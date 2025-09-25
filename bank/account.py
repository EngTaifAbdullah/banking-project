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


        if self.balance - amount < -100:       # this is overdraft logic
            raise ValueError("Withdrawal denied !! (limit -100 reached)")


        if self.balance < amount:              # this is overdraft case
            if self.overdraft_count >= 2:

                raise ValueError("Error!! Overdraft limit reached")
            
            fee = 35
            total = amount + fee

            if self.balance - total < -100:
                raise ValueError("Withdrawal denied !! (limit -100 reached)")
            
            self.balance -= total
            self.overdraft_count += 1

        else:
            self.balance -= amount

        return self.balance

# --------------------------------------------------------------------------------

    def get_balance(self):
        return self.balance

    

# python -m bank.account