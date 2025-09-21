import unittest

class TestSavingsAccount (unittest.TestCase):
    def test_deposit_into_savings (self) :
        customer = Customer ('1001', 'Taif', 'Abdullah')
        account = Account (checking=0, savings=0)
