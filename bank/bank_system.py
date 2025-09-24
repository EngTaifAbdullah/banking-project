#--------------------------------------- INCLOUD INFORMATIONS ABOUT SYSTEM  ---------------------------------------

import csv
import os
from bank.customer import Customer



class BankSystem:

    def __init__(self, filename="data/bank.csv"):
        self.filename = filename
        self.customers = {}
        self.load_customers()



# ---------------------------------------------------------  Add New Customer  ---------------------------------------------------------


    def add_customer(self, first_name, last_name, password, checking_balance=0, savings_balance=0):

        new_id = str(10000 + len(self.customers) + 1)

        new_customer = Customer(new_id, first_name, last_name, password, checking_balance, savings_balance)

        self.customers[new_id] = new_customer
        self.save_customer_to_csv(new_customer)

        return new_customer


# ---------------------------------------------------------------------------------------------------------------------------------------

# python -m bank.bank_system


