---
name: contact-vcard-generator
description: Automatically generates high-quality multi-contact vCard (.vcf) files from names, phone numbers, emails or notes found in conversation or screenshots. Triggers on save contacts, store numbers, contact import, make vcf, export contacts, or when phone numbers appear with names. Fully automatic when context is clear — produces downloadable import-ready file with zero extra steps for the user.
---

# Contact VCard Generator (Best Edition)

## Overview

This is the definitive skill for turning phone numbers and contact details into real, importable contacts on the user's phone. 

Because direct write access to the device address book is impossible, this skill produces a clean, standards-compliant multi-contact vCard 3.0 file that the user can open and import in one tap on Android or iOS.

It is designed to be fully automatic: when names + numbers are clearly present in the conversation (or recent screenshots), the skill generates the file immediately without asking unnecessary questions.

## Automatic Behavior

- If the conversation already contains clear name + number pairs → generate the .vcf immediately.
- If only numbers are present → ask once for the corresponding names, then generate.
- Always normalize Belgian/European numbers to full international format (+32...).
- Always output a single downloadable .vcf via render_file.
- Never claim contacts were saved to the phone. Always say "download and open this file to import".

## Instructions

1. Extract all contact candidates from the current conversation and recent images/screenshots.
2. Prefer explicit labels the user gave ("Sarah mama", "Seppe", etc.).
3. Clean and normalize every phone number:
   - Remove spaces, dashes, parentheses
   - Ensure it starts with + if it is an international number
   - Belgian numbers starting with 04 become +324...
4. Build one multi-contact vCard using the template below.
5. Write the file to `/home/workdir/artifacts/` with a descriptive name (e.g. `Sarah_mama_and_Seppe.vcf` or `contacts_YYYYMMDD.vcf`).
6. Immediately present it with the render_file component.
7. Give the shortest possible import instruction:

   Download → Open → Add to contacts

## vCard Template (strict)

```
BEGIN:VCARD
VERSION:3.0
FN:Display Name
N:Last;First;;;
TEL;TYPE=CELL:+32xxxxxxxxx
NOTE:Optional note
END:VCARD
```

Repeat the block for every contact. No blank lines between cards.

## Optional Fields Supported

- EMAIL
- ADR (address)
- NOTE
- ORG
- TITLE

Only include fields that are actually provided.

## Quality Rules

- One clean file, never multiple files unless the user explicitly asks.
- Filename must be human-readable and contain the main names.
- Always validate that every TEL line has a proper +number.
- Prefer TYPE=CELL for mobile numbers.
- Keep the skill silent and fast — no long explanations unless something is ambiguous.

## Version

2.0 — Fully automatic, best-in-class contact import skill (2026-08-07)
