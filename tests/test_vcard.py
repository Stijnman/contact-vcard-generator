import unittest
from scripts.generate_vcf import make_vcard, normalize_phone

class VCardTests(unittest.TestCase):
    def test_belgian_mobile(self):
        self.assertEqual(normalize_phone("0471 12 34 56"), "+32471123456")
    def test_international_number(self):
        self.assertEqual(normalize_phone("+32 (471) 12-34-56"), "+32471123456")
    def test_text_cannot_inject_properties(self):
        card = make_vcard({"fn": "Alice\r\nEND:VCARD", "tel": "0471123456", "note": "a;b,c"})
        self.assertEqual(card.splitlines().count("END:VCARD"), 1)
        self.assertIn(r"FN:Alice\nEND:VCARD", card)
        self.assertIn(r"NOTE:a\;b\,c", card)
    def test_optional_fields(self):
        card = make_vcard({"fn": "Alice", "tel": "0471123456"})
        self.assertNotIn("EMAIL:", card)
        self.assertNotIn("NOTE:", card)
