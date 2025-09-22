#--------------------------------------- INCLOUD THE TEST FOR ACCOUNT  ---------------------------------------


import unittest

from bank.account import Account

class TestAccount(unittest.TestCase):

# ----------- Deposit Test  -----------

    def test_deposit(self):
        acc = Account("10001", "checking" , 600)
        acc.deposit(300)
        self.assertEqual(acc.get_balance(), 900)

# ----------- Withdraw Test  -----------

    def test_withdraw_normal(self):
        acc = Account("10006", "savings", 2000)
        acc.withdraw(500)
        self.assertEqual(acc.get_balance(), 1500)


if __name__ == "__main__":
    unittest.main()
