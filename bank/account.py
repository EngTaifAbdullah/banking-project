#--------------------------------------- INCLOUD INFORMATIONS ABOUT USER ACCOUNT ---------------------------------------

class Account:

    def __init__(self, account_id, account_type, balance=0):
        
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.overdraft_count = 0
        self.active = True


# --------------------- Deposit ---------------------

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
        
        else:
            raise ValueError("The deposited amount must be greater than ZERO!")
        
        return self.balance

# --------------------- Withdraw ---------------------

    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount

        else:
           raise ValueError("Sorry! insufficient balance")
        return self.balance

# ------------------------------------------------------

    def get_balance(self):

        return self.balance

