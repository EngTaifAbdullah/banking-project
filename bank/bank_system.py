#----------------------------------------------  BANK SYSTEM  -------------------------------------------------

import csv
import os
from bank.customer import Customer


class BankSystem:

    def __init__(self, filename="data/bank.csv"):
        self.filename = filename
        self.customers = {}
        self.load_customers()

# ----------------------------------------------- Add New Customer -----------------------------------------------


    def add_customer(self, first_name, last_name, password, checking_balance=0, savings_balance=0):

        new_id = str(10000 + len(self.customers) + 1)
        new_customer = Customer(new_id, first_name, last_name, password, checking_balance, savings_balance)

        self.customers[new_id] = new_customer
        self._rewrite_all_customers()  
        return new_customer


# ------------------------------------------- Load Customers To CSV File --------------------------------------------


    def load_customers(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, mode="r") as file:
         reader = csv.DictReader(file)
         for row in reader:
            customer = Customer(
                row["account_id"],
                row["first_name"],
                row["last_name"],
                row["password"],
                int(row["checking_balance"]),
                int(row["savings_balance"]),
                row.get("active", "True") == "True",
                int(row.get("overdraft_count", 0))
            )
            self.customers[row["account_id"]] = customer

    
# --------------------------------------------- Find Customer by ID  ---------------------------------------------


    def find_customer(self, account_id):
        return self.customers.get(account_id)


# ----------------------------------------- Transfer Between Customers -----------------------------------------


    def transfer_between_customers(self, from_id, to_id, from_account, amount):

        sender = self.find_customer(from_id)
        receiver = self.find_customer(to_id)

        if not sender:
            raise ValueError(f"Sender with ID {from_id} not found")
        if not receiver:
            raise ValueError(f"Receiver with ID {to_id} not found")

        sender.transfer_to_another_customer(receiver, from_account, amount)

        self._rewrite_all_customers()


 # ------------------------------------ Rewrite All Customers ( Update CSV ) -----------------------------------


    def _rewrite_all_customers(self): # this method To avoid duplicates

     with open(self.filename, mode="w", newline="") as file:
         writer = csv.writer(file)
         writer.writerow([
            "account_id", "first_name", "last_name", "password", "checking_balance", "savings_balance", "active", "overdraft_count"
        ])
         for customer in self.customers.values():
            writer.writerow([
                customer.account_id,
                customer.first_name,
                customer.last_name,
                customer.password,
                customer.checking_account.get_balance(),
                customer.savings_account.get_balance(),
                customer.checking_account.active,   
                customer.checking_account.overdraft_count  
            ])
            
# -----------------------------------------------------------------------------------------------------------------