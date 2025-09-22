#--------------------------------------- INCLOUD THE TEST FOR ACCOUNT  ---------------------------------------

import unittest
from bank.account import Account



class TestAccount(unittest.TestCase):

    def setUp(self):

        self.acc = Account("10001", "checking", 1000)

# -------------------------- Valid Deposit Test  --------------------------


    def test_deposit_valid(self):

        self.acc.deposit(500)
        self.assertEqual(self.acc.get_balance(), 1500)


# -------------------------- Invalid Deposit Test  --------------------------











# -------------------------- Valid Withdraw Test  --------------------------

    def test_withdraw_valid(self):
        
        self.acc.withdraw(900)
        self.assertEqual(self.acc.get_balance(), 100)



# -------------------------- Invalid Withdraw Test  --------------------------





# ------------------------ Withdraw Overdraft Test  ------------------------






# -------------------- Withdraw Deactivation Test --------------------------





# -------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
