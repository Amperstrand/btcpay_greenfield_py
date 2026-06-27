#!/usr/bin/env bash
# Regenerate the Python client from swagger.json and assert the result
# matches what is committed under btcpay_greenfield_py/.
#
# The committed pyproject.toml and README.md are hand-curated, so this
# script only diffs the generated Python package itself.
#
# Exit codes:
#   0  regenerated output matches committed code
#   1  drift detected — run scripts/regenerate.sh locally and commit
#   2  generator failed
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo ">> patching swagger.json (upstream spec workarounds, in sandbox only)"
# Apply the same patches to a sandbox copy so committed swagger.json is preserved
SANDBOX_SPEC="$WORK/swagger.json"
cp swagger.json "$SANDBOX_SPEC"
cp openapi-python-client.config.yaml "$WORK/"

# Run patch on the sandbox copy
python3 - <<'PY' "$SANDBOX_SPEC"
import json, sys
from pathlib import Path
spec_path = Path(sys.argv[1])
spec = json.loads(spec_path.read_text())
schemas = spec.get("components", {}).get("schemas", {})
md = schemas.get("InvoiceMetadata")
if md and "anyOf" in md:
    md.pop("anyOf", None)
    md["type"] = "object"
    md["additionalProperties"] = True
spec_path.write_text(json.dumps(spec, indent=2) + "\n")
print("patched sandbox spec")
PY

echo ">> regenerating in $WORK"
pushd "$WORK" > /dev/null
python3 -m openapi_python_client generate \
    --path swagger.json \
    --config openapi-python-client.config.yaml \
    > regen.log 2>&1 || {
        cat regen.log
        echo "!! openapi-python-client failed (exit $?)"
        popd > /dev/null
        exit 2
    }
popd > /dev/null

# The generator emits a directory whose name comes from project_name_override.
GENERATED_DIR="$WORK/btcpay-greenfield-py/btcpay_greenfield_py"
if [[ ! -d "$GENERATED_DIR" ]]; then
    echo "!! expected generated package at $GENERATED_DIR not found"
    echo "!! generator output:"
    find "$WORK" -maxdepth 3 -type d
    exit 2
fi

# Apply the same post-processing the in-place regen does so the diff reflects
# what scripts/regenerate.sh actually commits. We delegate to the same script
# so the two paths can never drift out of sync.
echo ">> post-processing sandbox output (matches regenerate.sh step)"
python3 "$ROOT/scripts/post_process_generated.py" "$GENERATED_DIR"

echo ">> diffing $GENERATED_DIR against committed btcpay_greenfield_py/"
# Use rsync-style exclude for __pycache__ since diff -r doesn't have --exclude
# Walk the generated tree and compare file-by-file, skipping __pycache__
DRIFT=0
while IFS= read -r -d '' gen_file; do
    rel="${gen_file#$GENERATED_DIR/}"
    commit_file="btcpay_greenfield_py/$rel"
    if [[ ! -f "$commit_file" ]]; then
        echo "ONLY IN GENERATED: $rel"
        DRIFT=1
    elif ! diff -q "$gen_file" "$commit_file" > /dev/null; then
        echo "DIFFERS: $rel"
        DRIFT=1
    fi
done < <(find "$GENERATED_DIR" -type f -not -path '*/__pycache__/*' -print0)

# Also check for files in committed that aren't in generated
while IFS= read -r -d '' commit_file; do
    rel="${commit_file#btcpay_greenfield_py/}"
    gen_file="$GENERATED_DIR/$rel"
    if [[ ! -f "$gen_file" ]]; then
        echo "ONLY IN COMMITTED: $rel"
        DRIFT=1
    fi
done < <(find btcpay_greenfield_py -type f -not -path '*/__pycache__/*' -print0)

if [[ "$DRIFT" -eq 0 ]]; then
    echo "OK: no drift"
    exit 0
else
    echo ""
    echo "!! drift detected between swagger.json and committed btcpay_greenfield_py/"
    echo "!! To fix:"
    echo "!!   ./scripts/regenerate.sh"
    echo "!!   git add btcpay_greenfield_py/"
    echo "!!   git commit -m 'chore: regenerate client from swagger.json'"
    exit 1
fi
