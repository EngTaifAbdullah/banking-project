#--------------------------------------- INCLOUD THE TEST FOR ACCOUNT  ---------------------------------------

import unittest
from bank.account import Account



class TestAccount(unittest.TestCase):

# ----------------------------- Deposit Test  -----------------------------

     def test_deposit(self):

        acc = Account("10001", "checking", 1500)
        acc.deposit(500)
        self.assertEqual(acc.get_balance(), 2000)


# ----------------------------- Withdraw Test  -----------------------------

     def test_withdraw(self):

        acc = Account("10006", "savings", 300)
        acc.withdraw(200)
        self.assertEqual(acc.get_balance(), 100)

# ------------------------ Withdraw Overdraft Test  ------------------------






# -------------------- Withdraw Deactivation Test --------------------------





# -------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
