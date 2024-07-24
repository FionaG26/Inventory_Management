import unittest
import pandas as pd
from scripts.inventory_management import load_data, insert_data, get_high_value_laptops
from database import create_connection

class TestInventoryManagement(unittest.TestCase):
    def setUp(self):
        self.connection = create_connection()
        self.df = pd.DataFrame({
            'id': [1, 2],
            'brand': ['Dell', 'Apple'],
            'model': ['XPS 15', 'MacBook Pro'],
            'price': [1200, 2500]
        })
        insert_data(self.connection, self.df)

    def test_load_data(self):
        df = load_data('data/sample_data.csv')
        self.assertGreater(len(df), 0)

    def test_get_high_value_laptops(self):
        laptops = get_high_value_laptops(self.connection)
        self.assertGreater(len(laptops), 0)
        self.assertTrue(all(laptop['price'] > 1000 for laptop in laptops))

if __name__ == '__main__':
    unittest.main()
