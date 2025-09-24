# ------------------------------------------- INCLOUD THE TEST FOR BANK SYSTEM  -----------------------------------------------


import unittest
import os
from bank.bank_system import BankSystem


class TestBankSystem(unittest.TestCase):


# ------------------------------------------  Add and find Customer TEST  ------------------------------------------


    def test_add_customer_and_find(self):

        test_file = "test_bank.csv"
        if os.path.exists(test_file):
            os.remove(test_file)

        bank = BankSystem(filename=test_file)

        new_customer = bank.add_customer("Ali", "Saleh", "1234", 1000, 500)

        self.assertEqual(new_customer.first_name, "Ali")
        self.assertEqual(new_customer.checking_account.get_balance(), 1000)


        found = bank.find_customer(new_customer.account_id)
        self.assertIsNotNone(found)
        self.assertEqual(found.last_name, "Saleh")

        if os.path.exists(test_file):
            os.remove(test_file)


# -----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()


# python -m test.test_bank_system
