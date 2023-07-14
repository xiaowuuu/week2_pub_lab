import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.name = "Holyrood 9A"
        self.till = 500
        self.drink_to_buy = ("peach beer", 6)    
    
    def test_pub_has_name(self):
        self.assertEqual("Holyrood 9A", self.name) 

    @unittest.skip("delete this line to run the test")
    def test_sell_drink(self):
        self.assertEqual( )
