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

# ----------------------------------------------------------------------
