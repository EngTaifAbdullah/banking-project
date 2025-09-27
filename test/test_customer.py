#----------------------------------------- INCLOUD THE TEST FOR CUSTOMER -----------------------------------------

import unittest
from bank.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):

        self.customer1 = Customer("10001", "Taif", "Abdullah", "12345", 1500, 300) # Taif 's account 
        self.customer2 = Customer("10002", "Rose", "Abdullah", "idh3FGd", 3000, 500) # Another user  



# ------------------------------------------------------ Login Page  -----------------------------------------------------


    def test_login_success(self):
        self.assertTrue(self.customer1.login("12345"))

    def test_login_fail(self):
        self.assertFalse(self.customer1.login("dcfgvhbjnkftgy"))  # if the user enterd wrong password


# ------------------------------------------------- Deposit in Checking -------------------------------------------------


    def test_deposit_checking(self):

        self.customer1.deposit_to_checking(500)
        self.assertEqual(self.customer1.checking_account.get_balance(), 2000)


# ------------------------------------------------- Withdraw in Saving -------------------------------------------------


    def test_withdraw_savings(self):
        
        self.customer1.withdraw_from_savings(200)
        self.assertEqual(self.customer1.savings_account.get_balance(), 100)


# ------------------------------------------------- Transfer to Saving  -------------------------------------------------


    def test_transfer_to_savings(self):

        self.customer1.transfer_to_savings(500)
        self.assertEqual(self.customer1.checking_account.get_balance(), 1000)
        self.assertEqual(self.customer1.savings_account.get_balance(), 800)


# ------------------------------------------------- Transfer to Checking -------------------------------------------------


    def test_transfer_to_checking(self):

        self.customer1.transfer_to_checking(100)
        self.assertEqual(self.customer1.checking_account.get_balance(), 1600)
        self.assertEqual(self.customer1.savings_account.get_balance(), 200)


# ------------------------------------------------- Transfer to Another User ------------------------------------------------


    def test_transfer_to_another_customer_checking(self):

        self.customer1.transfer_to_another_customer(self.customer2, "checking", 500)
        self.assertEqual(self.customer1.checking_account.get_balance(), 1000)
        self.assertEqual(self.customer2.checking_account.get_balance(), 3500)



    def test_transfer_to_another_customer_savings(self):

        self.customer1.transfer_to_another_customer(self.customer2, "savings", 100)
        self.assertEqual(self.customer1.savings_account.get_balance(), 200)
        self.assertEqual(self.customer2.savings_account.get_balance(), 600)


# ------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

# python -m test.test_customer