#--------------------------------------- INCLOUD INFORMATIONS ABOUT USER ACCOUNT ---------------------------------------

class Account:

    def __init__(self, account_id, account_type, balance=0, active=True, overdraft_count=0):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.active = active
        self.overdraft_count = overdraft_count



# -------------------------------------- Deposit -------------------------------------


    def deposit(self, amount):

        if not self.active:
            raise ValueError("Account is deactivated ❌")
        
        if amount > 0:
            self.balance += amount

        else:
            raise ValueError("The deposited amount must be greater than ZERO!")
        return self.balance


# -------------------------------------- Withdraw --------------------------------------


    def withdraw(self, amount):

        if not self.active:
            raise ValueError("This account is deactivated")

        if amount <= 0:
            raise ValueError("Withdrawal must be greater than ZERO!")

        if self.balance >= amount:
           self.balance -= amount
           return self.balance


        fee = 35
        total = amount + fee
        new_balance = self.balance - total


        if new_balance < -100:  
          self.active = False
          raise ValueError("Withdrawal denied!! Limit -100 reached. Account Deactivated.")



        self.balance = new_balance
        self.overdraft_count += 1


        if self.overdraft_count >= 2:
           self.active = False
 
          

        return self.balance

# --------------------------------------------------------------------------------

    def get_balance(self):
        return self.balance

    

# python -m bank.account