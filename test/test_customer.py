#--------------------------------------- INCLOUD THE TEST FOR CUSTOMER ---------------------------------------

import unittest
from bank.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("10001", "Taif", "Abdullah", "12345", 1500, 300) # Taif 's account 

# ----------------------------- Login -----------------------------

    def test_login_success(self):
        self.assertTrue(self.customer.login("12345"))

    def test_login_fail(self):
        self.assertFalse(self.customer.login("dcfgvhbjnkftgy"))  # if the user enterd wrong password
# -----------------------------
