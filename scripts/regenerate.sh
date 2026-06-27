#!/usr/bin/env bash
# Regenerate the Python client in-place from swagger.json.
# Use this locally when regenerate-and-diff.sh reports drift.
#
# NOTE: this overwrites btcpay_greenfield_py/ but leaves the hand-curated
# pyproject.toml and README.md untouched.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo ">> patching swagger.json (upstream spec workarounds)"
python3 scripts/patch_swagger.py

echo ">> regenerating in $WORK"
cp swagger.json "$WORK/"
cp openapi-python-client.config.yaml "$WORK/"
pushd "$WORK" > /dev/null
python3 -m openapi_python_client generate \
    --path swagger.json \
    --config openapi-python-client.config.yaml \
    > regen.log 2>&1 || {
        cat regen.log
        popd > /dev/null
        exit 1
    }
popd > /dev/null

GENERATED_PACKAGE="$WORK/btcpay-greenfield-py/btcpay_greenfield_py"
if [[ ! -d "$GENERATED_PACKAGE" ]]; then
    echo "!! generated package not found at $GENERATED_PACKAGE"
    find "$WORK" -maxdepth 3 -type d
    exit 1
fi

echo ">> replacing btcpay_greenfield_py/ in place"
rm -rf btcpay_greenfield_py
cp -R "$GENERATED_PACKAGE" btcpay_greenfield_py

echo ">> post-processing generated code (fix _parse_response empty-body crash)"
python3 scripts/post_process_generated.py

echo ">> ruff check"
ruff check btcpay_greenfield_py/ || true

echo "OK: regenerated. Review with 'git diff' and commit."
