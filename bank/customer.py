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

# ----------- Password -----------

    def login(self, password):
     
        return self.password == password
  