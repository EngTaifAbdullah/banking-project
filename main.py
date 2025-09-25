from bank.bank_system import BankSystem

def main():
    bank = BankSystem(filename="data/bank.csv")

    while True:
        print("\n--------------------------- Welcome to Bank System ----------------------------")

        print("1. Add New Customer")
        print("2. Login")
        print("3. Exit")

        choice = input("🔹 Please Enter the service: ")


# python main.py