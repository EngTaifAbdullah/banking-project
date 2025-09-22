#--------------------------------------- INCLOUD THE TEST FOR CUSTOMER ---------------------------------------

import unittest
from bank.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("10001", "Taif", "Abdullah", "12345", 1500, 300) # Taif 's account 



# ---------------------------------- Login Page  ----------------------------------


    def test_login_success(self):
        self.assertTrue(self.customer.login("12345"))

    def test_login_fail(self):
        self.assertFalse(self.customer.login("dcfgvhbjnkftgy"))  # if the user enterd wrong password


# ----------------------------- Deposit in Checking -----------------------------


    def test_deposit_checking(self):

        self.customer.deposit_to_checking(500)
        self.assertEqual(self.customer.checking_account.get_balance(), 2000)


# ----------------------------- Withdraw in Saving -----------------------------


    def test_withdraw_savings(self):
        
        self.customer.withdraw_from_savings(200)
        self.assertEqual(self.customer.savings_account.get_balance(), 100)


# ----------------------------- Transfer to Saving  -----------------------------


    def test_transfer_to_savings(self):

        self.customer.transfer_to_savings(500)
        self.assertEqual(self.customer.checking_account.get_balance(), 1000)
        self.assertEqual(self.customer.savings_account.get_balance(), 800)


# ---------------------------- Transfer to Checking ----------------------------






# ------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()