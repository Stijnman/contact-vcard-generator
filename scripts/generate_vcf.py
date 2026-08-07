#!/usr/bin/env python3
"""
Clean vCard 3.0 generator.
Usage: python generate_vcf.py --output /path/to/file.vcf --contacts '[{"fn":"Name","tel":"+32..."}]'
"""

import argparse
import json
import re
from pathlib import Path

def normalize_phone(phone: str) -> str:
    phone = re.sub(r"[\s\-\(\)]", "", phone)
    if phone.startswith("04") and len(phone) == 10:
        phone = "+32" + phone[1:]
    if not phone.startswith("+"):
        phone = "+" + phone
    return phone

def make_vcard(contact: dict) -> str:
    fn = contact.get("fn", "Unknown").strip()
    tel = normalize_phone(contact.get("tel", ""))
    note = contact.get("note", "").strip()
    email = contact.get("email", "").strip()

    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{fn}",
        f"N:;{fn};;;",
        f"TEL;TYPE=CELL:{tel}",
    ]
    if email:
        lines.append(f"EMAIL:{email}")
    if note:
        lines.append(f"NOTE:{note}")
    lines.append("END:VCARD")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--contacts", required=True, help="JSON list of contacts")
    args = parser.parse_args()

    contacts = json.loads(args.contacts)
    cards = [make_vcard(c) for c in contacts]
    content = "\n".join(cards) + "\n"

    Path(args.output).write_text(content, encoding="utf-8")
    print(f"Wrote {len(contacts)} contacts to {args.output}")

if __name__ == "__main__":
    main()
