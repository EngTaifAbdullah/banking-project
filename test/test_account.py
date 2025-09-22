#--------------------------------------- INCLOUD THE TEST FOR ACCOUNT  ---------------------------------------

import unittest
from bank.account import Account



class TestAccount(unittest.TestCase):

# ----------------------------- Deposit Test  -----------------------------

     def test_deposit(self):

        acc = Account("10001", "checking", 1000)
        acc.deposit(500)
        self.assertEqual(acc.get_balance(), 1500)


# ----------------------------- Withdraw Test  -----------------------------

     def test_withdraw_normal(self):

        acc = Account("10006", "savings", 500)
        acc.withdraw(200)
        self.assertEqual(acc.get_balance(), 300)

# ------------------------ Withdraw Overdraft Test  ------------------------






# -------------------- Withdraw Deactivation Test --------------------------





# -------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
