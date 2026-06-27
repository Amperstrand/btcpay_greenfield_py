#!/usr/bin/env python3
"""Patch swagger.json to work around upstream spec issues that produce broken codegen.

Patches applied
---------------
1. InvoiceMetadata has an anyOf with title-bearing subschemas ("Point of Sale (Cart view)",
   "Order information", etc.) that openapi-python-client cannot disambiguate — it produces
   duplicate model names and ends up emitting a broken runtime import in the surviving
   model's to_dict() (it references a module that the generator refused to write).

   Fix: replace the anyOf with `additionalProperties: true` (the schema is documented as
   freeform anyway: "you can introduce any json format you wish").

Run this before openapi-python-client generate. scripts/regenerate.sh does it for you.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "swagger.json"


def patch(spec: dict) -> int:
    patches_applied = 0
    schemas = spec.get("components", {}).get("schemas", {})

    # --- Patch 1: flatten InvoiceMetadata to a plain freeform object ---
    md = schemas.get("InvoiceMetadata")
    if md and "anyOf" in md:
        # Preserve the description and example, drop the conflicting anyOf.
        md.pop("anyOf", None)
        md["type"] = "object"
        md["additionalProperties"] = True
        patches_applied += 1

    return patches_applied


def main() -> int:
    if not SPEC.exists():
        print(f"!! {SPEC} not found", file=sys.stderr)
        return 2

    spec = json.loads(SPEC.read_text())
    count = patch(spec)
    SPEC.write_text(json.dumps(spec, indent=2) + "\n")
    print(f"OK: applied {count} patch(es) to {SPEC.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
