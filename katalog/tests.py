from django.test import TestCase
from katalog.models import CatalogItem
from django.forms.models import model_to_dict

# Create your tests here.

class KatalogTestCases(TestCase):
    fixtures = ['initial_catalog_data.json']

    def test_data_specified_key(self):
        data = model_to_dict(CatalogItem.objects.first())
        self.assertTrue("item_name" in data)
        self.assertTrue("item_price" in data)
        self.assertTrue("description" in data)
        self.assertTrue("item_stock" in data)
        self.assertTrue("rating" in data)
        self.assertTrue("item_url" in data)

    def test_data_correct_type(self):
        data = CatalogItem.objects.all()
        for test_data in data:
            self.assertTrue(isinstance(test_data.item_name, str))
            self.assertTrue(isinstance(test_data.item_price, str))
            self.assertTrue(isinstance(test_data.description, str))
            self.assertTrue(isinstance(test_data.item_stock, str))
            self.assertTrue(isinstance(test_data.rating, str))
            self.assertTrue(isinstance(test_data.item_url, str))