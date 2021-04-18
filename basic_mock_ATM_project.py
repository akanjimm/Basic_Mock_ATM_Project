from datetime import datetime
name = input('What is your name? \n')
allowed_users = ['Seyi', 'Mike', 'Love']
allowed_passwords = ['passwordSeyi', 'passwordMike', 'passwordLove']
account_balances = [2000, 3000, 1000]

if name in allowed_users:
    password = input('Your password? \n')
    user_id = allowed_users.index(name)

    if password == allowed_passwords[user_id]:
        print(datetime.now().strftime("%d-%B-%Y   %I:%M:%S %p"))
        print("Welcome %s" %name)
        
        print("These are the available options.")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        selected_option = int(input("Please select an option: "))

        if selected_option == 1:
            print("You selected %s" %selected_option)
            amount_to_withdraw = input("How much would you like to withdraw? ")
            print("Take your cash")

        elif selected_option == 2:
            print("You selected %s" %selected_option)
            amount_deposited = float(input("How much would you like to deposit? "))
            current_balance = account_balances[user_id] + amount_deposited
            account_balances[user_id] = current_balance
            print("Your current balance is ₦%s" %current_balance)

        elif selected_option == 3:
            print("You selected %s" %selected_option)
            complaint = input("What issue will you like to report? \n")
            print("Thank you for contacting us")

        else:
            print("Invalid option selected")

    else:
        print("Password Incorrect, please try again")

else:
    print("Name not found, please try again")
