# ------------------------------------------------------------ INCLOUD INFORMATIONS ABOUT THE CUSTEOMER ------------------------------------------------------------

from bank.account import Account

class Customer:
    def __init__(self, account_id, first_name, last_name, password, checking_balance=0, savings_balance=0, active=True, overdraft_count=0):

        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
        self.checking_account = Account(account_id, "checking", checking_balance, active, overdraft_count)
        self.savings_account = Account(account_id, "savings", savings_balance, active, overdraft_count)



# -------------------------------------------------------------- Password --------------------------------------------------------------


    def login(self, password):
     
     if not self.checking_account.active:  
        return False  
     return self.password == password


# ----------------------------------------------------- Deposit (checking, saving) -----------------------------------------------------


    def deposit_to_checking(self, amount):
        return self.checking_account.deposit(amount)


    def deposit_to_savings(self, amount):
        return self.savings_account.deposit(amount)
    

# ----------------------------------------------------- Withdraw (checking, saving) -----------------------------------------------------


    def withdraw_from_checking(self, amount):
        return self.checking_account.withdraw(amount)


    def withdraw_from_savings(self, amount):
        return self.savings_account.withdraw(amount)
    
    
# ----------------------------------------------------- Transfer (checking, saving) -----------------------------------------------------


    def transfer_to_savings(self, amount):
       
        new_checking = self.checking_account.withdraw(amount)     # I take it the amount from checking (withdraw) 
        new_saving = self.savings_account.deposit(amount)         # I put it in saving (deposit)

        return new_checking, new_saving                           # updating the amount in saving and checking


    def transfer_to_checking(self, amount):

        new_saving = self.savings_account.withdraw(amount)
        new_checking = self.checking_account.deposit(amount)
        
        
        return new_checking, new_saving


# ----------------------------------------------------- Transfer to another User -----------------------------------------------------


    def transfer_to_another_customer(self, target_customer, from_account, amount): 

        if from_account == "checking":
            self.checking_account.withdraw(amount)
            target_customer.checking_account.deposit(amount) # take the money from Mychacking (withdraw) and trasnfer to user (dapost)


        elif from_account == "savings":             # Here I added 2 way to transfer to another user (transfer from saving or checking)
            self.savings_account.withdraw(amount)
            target_customer.checking_account.deposit(amount)
            

        else:
            raise ValueError("Invalid Account Type")


# ---------------------------------------------------------------------------------------------------------------------------------------

# python -m bank.customer