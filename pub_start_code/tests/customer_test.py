import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Ying", 25, 30, 0)
        self.drink_to_buy = Drink("beer", 4, 1)
    def test_customer_has_name(self):
        self.assertEqual("Ying", self.customer.name)
    
    def test_reduced_wallet(self):
        self.assertEqual(22, self.customer.reduced_wallet)