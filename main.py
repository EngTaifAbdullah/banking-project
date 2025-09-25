

from bank.bank_system import BankSystem

def main():
    bank = BankSystem(filename="data/bank.csv")

    while True:
        print("\n------------------------------ Welcome to Bank System -------------------------------")
        print("1. Add New Customer")
        print("2. Login")
        print("3. Exit")

        choice = input("🔹 Please Enter the service: ")


        if choice == "1":
            first = input("First Name: ")
            last = input("Last Name: ")
            password = input("Password: ")
            checking = int(input("Initial Checking Balance: "))
            savings = int(input("Initial Savings Balance: "))

            customer = bank.add_customer(first, last, password, checking, savings)
            print(f"Customer Added successfully with ID: {customer.account_id} ✅")



if __name__ == "__main__":
    main()


# python main.py