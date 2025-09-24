#--------------------------------------- INCLOUD INFORMATIONS ABOUT SYSTEM  ---------------------------------------

import csv
import os
from bank.customer import Customer


class BankSystem:

    def __init__(self, filename="bank.csv"):

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

# -----------------------------------------------------  Save Customer to CSV file  -----------------------------------------------------


    def save_customer_to_csv(self, customer):
        file_exists = os.path.isfile(self.filename)

        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)


            if not file_exists:
                writer.writerow(["account_id", "first_name", "last_name", "password", "checking_balance", "savings_balance"])


            writer.writerow([
                customer.account_id,
                customer.first_name,
                customer.last_name,
                customer.password,
                customer.checking_account.get_balance(),
                customer.savings_account.get_balance()
            ])
