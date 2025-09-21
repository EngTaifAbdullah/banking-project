import unittest
import os
import tempfile
import csv

from bank.bank_system import BankSystem

class TestBankSystemCSV(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.bank_csv = os.path.join(self.temp_dir.name, "bank.csv")
        self.tx_csv = os.path.join(self.temp_dir.name, "transactions.csv")
        self.bs = BankSystem(bank_csv=self.bank_csv, tx_csv=self.tx_csv)



if __name__ == '__main__':
    unittest.main()
