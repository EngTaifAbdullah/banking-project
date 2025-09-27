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
            try:
                first = input("First Name: ")
                last = input("Last Name: ")
                password = input("Password: ")
                checking = int(input("Initial Checking Balance: "))
                savings = int(input("Initial Savings Balance: "))

                customer = bank.add_customer(first, last, password, checking, savings)
                print(f"Customer Added Successfully with ID: {customer.account_id} ✅")
                
            except Exception as e:
                print(f" Error: {e}")



        elif choice == "2":
            account_id = input("Enter Account ID: ")
            password = input("Enter Password: ")
            customer = bank.find_customer(account_id)

            if customer and customer.login(password):
                print(f"\nWelcome ( {customer.first_name} {customer.last_name} ) ✨ !")

                while True:
                    print("\n----------------------------------- Customer Menu -----------------------------------")
                    print("1. View Balances")
                    print("2. Deposit to Checking")
                    print("3. Deposit to Savings")
                    print("4. Withdraw from Checking")
                    print("5. Withdraw from Savings")
                    print("6. Transfer between my accounts (Checking\\Savings)")
                    print("7. Transfer to Another Customer")
                    print("8. Logout")
                    print("-----------------------------------")
                    sub_choice = input("🔹 Please Enter the service: ")

                    try:
                        if sub_choice == "1":
                            print(f"Checking Balance: {customer.checking_account.get_balance()} 💵")
                            print(f"Savings Balance: {customer.savings_account.get_balance()} 💵")


                        elif sub_choice == "2":
                            amount = int(input("Enter Amount to Deposit in Checking: "))
                            customer.deposit_to_checking(amount)
                            bank._rewrite_all_customers()
                            print("Deposit Successful ✅ !")


                        elif sub_choice == "3":
                            amount = int(input("Enter Amount to Deposit in Savings: "))
                            customer.deposit_to_savings(amount)
                            bank._rewrite_all_customers()
                            print("Deposit Successful ✅ !")


                        elif sub_choice == "4":
                            amount = int(input("Enter Amount to Withdraw from Checking: "))
                            customer.withdraw_from_checking(amount)
                            bank._rewrite_all_customers()
                            print("Withdrawal Successful ✅ !")


                        elif sub_choice == "5":
                            amount = int(input("Enter Amount to Withdraw from Savings: "))
                            customer.withdraw_from_savings(amount)
                            bank._rewrite_all_customers()
                            print("Withdrawal Successful ✅ !")


                        elif sub_choice == "6":
                            print("a) Checking To Savings")
                            print("b) Savings To Checking")
                            opt = input("Choose (a/b): ").lower()
                            amount = int(input("Enter Amount to Transfer: "))

                            if opt == "a":
                                customer.transfer_to_savings(amount)
                                bank._rewrite_all_customers()
                                print("Transfer To Savings Successful ✅ !")

                            elif opt == "b":
                                customer.transfer_to_checking(amount)
                                bank._rewrite_all_customers()
                                print("Transfer To Checking Successful ✅ !")

                            else:
                                print("Invalid Option ❌")



                        elif sub_choice == "7":
                            target_id = input("📍 Enter Target Customer ID: ")
                            from_account = input("📍 Transfer from (checking/savings): ").lower()
                            amount = int(input("📍 Enter Amount to Transfer: "))
                            bank.transfer_between_customers(customer.account_id, target_id, from_account, amount)
                            print(f"Transfer Successful! To Customer ID {target_id} ✅ ")

                        elif sub_choice == "8":
                            print("Logged out Successfully")
                            break

                        else:
                            print("Invalid choice, try again ❌")

                    except Exception as e:
                        print(f"Error: {e}")
            else:
                print("Invalid account ID or password ❌")

        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again ❌")


if __name__ == "__main__":
    main()

# python main.py
