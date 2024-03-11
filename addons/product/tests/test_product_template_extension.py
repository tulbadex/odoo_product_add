""" from odoo.tests.common import TransactionCase


class TestProductTemplateExtension(TransactionCase):
    def test_compute_slug(self):
        product = self.env['product.template'].create({'name': 'Test Product'})
        self.assertEqual(product.slug, 'test-product')

    def test_unique_additional_barcode(self):
        product1 = self.env['product.template'].create({'name': 'Test Product 1', 'additional_barcode': '123'})
        with self.assertRaises(Exception):
            product2 = self.env['product.template'].create({'name': 'Test Product 2', 'additional_barcode': '123'})
              """

from odoo.tests.common import TransactionCase


class TestProductTemplateExtension(TransactionCase):
    def test_compute_slug(self):
        product = self.env['product.template'].create({'name': 'Test Product'})
        expected_slug = 'test-product'
        self.assertEqual(product.slug, expected_slug, "Computed slug doesn't match expected value")

    def test_unique_additional_barcode(self):
        product1 = self.env['product.template'].create({'name': 'Test Product 1', 'additional_barcode': '123'})
        with self.assertRaises(Exception) as context:
            product2 = self.env['product.template'].create({'name': 'Test Product 2', 'additional_barcode': '123'})

        self.assertTrue("Additional barcode must be unique." in str(context.exception), "Exception message doesn't match expected value")