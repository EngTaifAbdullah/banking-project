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


    def test_withdraw_overdraft_once(self):

        acc = Account("10005", "checking", 50)
        acc.withdraw(70)  
        self.assertEqual(acc.get_balance(), -55)
        self.assertEqual(acc.overdraft_count, 1)



    def test_withdraw_overdraft_twice(self):

        acc = Account("10006", "checking", 0)
        acc.withdraw(50)  
        acc.withdraw(10)  

        with self.assertRaises(ValueError):
            acc.withdraw(5)


# ---------------------------------- Withdraw Deactivation Test ---------------------------------


    def test_account_deactivated(self):

        acc = Account("10007", "checking", 100, active=False)
        with self.assertRaises(ValueError):
            acc.deposit(50)
        with self.assertRaises(ValueError):
            acc.withdraw(10)


# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()


# python -m test.test_account