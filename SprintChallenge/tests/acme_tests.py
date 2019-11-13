import unittest

from src.acme import Product
from src.acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_stealability(self):
        """Test stealability of product with a price of 25 and weight of 50
        message should be 'Kinda stealable.'"""
        prod = Product(name='Test Product',
                       price=25,
                       weight=50)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_product_explosion(self):
        """Test explosion of product with flammability of 1.1 and weight
        of 100 message should be '...BABOOM!!' """
        prod = Product(name='Test Product',
                       flammability=1.1,
                       weight=100)
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    def test_default_number_of_products(self):
        """Test default number of products generated is 30"""
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

    def test_legal_name(self):
        prod_list = generate_products()
        for i in range(len(prod_list)):
            name = prod_list[i].name.split()
            self.assertIn(name[0], adjectives)
            self.assertIn(name[1], nouns)


if __name__ == '__main__':
    unittest.main()
