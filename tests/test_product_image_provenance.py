"""Keep public provenance distinct from verified image authorization."""
import copy
import json
import unittest
from pathlib import Path
from validate_product_cards import validate_registry

ROOT = Path(__file__).resolve().parents[1]

class ProductImageProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads((ROOT / '.content/products/registry.json').read_text())
        self.affiliate = json.loads((ROOT / '.content/products/affiliate.json').read_text())

    def test_public_source_can_be_recorded_without_claiming_authorization(self):
        validate_registry(self.registry, self.affiliate)
        image = self.registry['products']['supernote-manta']['image']
        self.assertFalse(image['rights_checked'])
        self.assertEqual(image['source_type'], 'MANUFACTURER_PUBLIC')

    def test_public_source_requires_provenance(self):
        for field in ('source_page', 'original_url', 'attribution', 'rights_basis'):
            registry = copy.deepcopy(self.registry)
            registry['products']['supernote-manta']['image'].pop(field)
            with self.subTest(field=field), self.assertRaises(SystemExit):
                validate_registry(registry, self.affiliate)

    def test_unverified_source_cannot_claim_verified_rights(self):
        image = self.registry['products']['supernote-manta']['image']
        image['rights_checked'] = True
        with self.assertRaises(SystemExit):
            validate_registry(self.registry, self.affiliate)

    def test_authorized_source_still_requires_checked_rights(self):
        image = self.registry['products']['supernote-manta']['image']
        image['source_type'] = 'MANUFACTURER_AUTHORIZED'
        with self.assertRaises(SystemExit):
            validate_registry(self.registry, self.affiliate)
