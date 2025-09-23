#--------------------------------------- INCLOUD THE TEST FOR ACCOUNT  ---------------------------------------

import unittest
from bank.account import Account



class TestAccount(unittest.TestCase):
    

# -----------------------------  Deposit Test (Checking, Saving)  -----------------------------


    def test_deposit_checking(self):

        acc = Account("10001", "checking", 1500)
        acc.deposit(500)
        self.assertEqual(acc.get_balance(), 2000)


    def test_deposit_savings(self):

        acc = Account("10002", "savings", 300)
        acc.deposit(200)
        self.assertEqual(acc.get_balance(), 500)


# -----------------------------  Withdraw Test (Checking, Saving)  -----------------------------


    def test_withdraw_checking(self):

        acc = Account("10003", "checking", 1500)
        acc.withdraw(300)
        self.assertEqual(acc.get_balance(), 1200)


    def test_withdraw_savings(self):

        acc = Account("10004", "savings", 300)
        acc.withdraw(100)
        self.assertEqual(acc.get_balance(), 200)


# ---------------------------------- Withdraw Overdraft Test  ----------------------------------




                       
# I'm still working in this part




# ---------------------------------- Withdraw Deactivation Test ---------------------------------





# I'm still working in this part




# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
