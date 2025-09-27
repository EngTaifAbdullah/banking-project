# ------------------------------------------------- INCLOUD THE TEST FOR BANK SYSTEM  ------------------------------------------------


import unittest
import os
from bank.bank_system import BankSystem


class TestBankSystem(unittest.TestCase):



# This method to ensure each test starts from scratch like new enviroment *no accumulated data from previous tests* empty file

    def setUp(self):
        self.test_file = "test_bank.csv"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.bank = BankSystem(filename=self.test_file)



# The goal of this method is to ensure that no unwanted files or data after the tests are completed, so use it the file the delete it

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


# ----------------------------------------------------  Add and find Customer TEST  ----------------------------------------------------



    def test_add_customer_and_find(self):
        
        new_customer = self.bank.add_customer("Taif", "Abdullah", "1234", 1000, 500)

        self.assertEqual(new_customer.first_name, "Taif")            # Ensure the adding and finding the customer is working succsusfully

        self.assertEqual(new_customer.checking_account.get_balance(), 1000)

        found = self.bank.find_customer(new_customer.account_id)     # looking for the account ID 

        self.assertIsNotNone(found)                                  # Ensure you are found it ( Compare information )

        self.assertEqual(found.last_name, "Abdullah")                # Ensure his last name  



# ---------------------------------------------------  Transfer Between Customers TEST  --------------------------------------------------


    def test_transfer_between_customers(self):

        c1 = self.bank.add_customer("Taif", "Abdullah", "1234", 1000, 500)
        c2 = self.bank.add_customer("Rose", "Abdullah", "5678", 300, 200)


        self.bank.transfer_between_customers(c1.account_id, c2.account_id, "checking", 200)

        self.assertEqual(c1.checking_account.get_balance(), 800)  
        self.assertEqual(c2.checking_account.get_balance(), 500)  


# ----------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()


# python -m test.test_bank_system
