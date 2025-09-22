#--------------------------------------- INCLOUD INFORMATIONS ABOUT USER ACCOUNT ---------------------------------------

class Account:
    def __init__(self, account_id, account_type, balance=0):
     
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance


# ----------- Deposit -----------

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
        
        else:
            raise ValueError("The deposited amount MUST be greater than zero!")
        return self.balance
    

