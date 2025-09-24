#--------------------------------------- INCLOUD INFORMATIONS ABOUT THE CUSTEOMER ---------------------------------------

from bank.account import Account

class Customer:
    def __init__(self, account_id, first_name, last_name, password, checking_balance=0, savings_balance=0):
      

        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        self.checking_account = Account(account_id, "checking", checking_balance)
        self.savings_account = Account(account_id, "savings", savings_balance)


# ----------------------------- Password -----------------------------


    def login(self, password):
     
        return self.password == password
    

# -------------------- Deposit (checking, saving) --------------------


    def deposit_to_checking(self, amount):
        return self.checking_account.deposit(amount)


    def deposit_to_savings(self, amount):
        return self.savings_account.deposit(amount)
    

# -------------------- Withdraw (checking, saving) --------------------


    def withdraw_from_checking(self, amount):
        return self.checking_account.withdraw(amount)


    def withdraw_from_savings(self, amount):
        return self.savings_account.withdraw(amount)
    
    
# -------------------- Transfer (checking, saving) --------------------


    def transfer_to_savings(self, amount):
       
        self.checking_account.withdraw(amount) 
        self.savings_account.deposit(amount)


    def transfer_to_checking(self, amount):
       
        self.savings_account.withdraw(amount)
        self.checking_account.deposit(amount)


# --------------------- Transfer to another User ---------------------


    def transfer_to_another_customer(self, target_customer, from_account, amount): 

        if from_account == "checking":
            self.checking_account.withdraw(amount)
            target_customer.checking_account.deposit(amount)


        elif from_account == "savings":  # Here I added 2 way to transfer to another user (transfer from saving or checking)
            self.savings_account.withdraw(amount)
            target_customer.savings_account.deposit(amount)
            

        else:
            raise ValueError("Invalid account type")


# ----------------------------------------------------------------------

# python -m bank.customer