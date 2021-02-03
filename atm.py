from operation import *
name = str(input("Please Enter your name :"))
while True:
    print("\nMenu\n(1)View Balance\n(2)Deposit amount\n(3)Withdraw amount\n(4)Quit")
    choice = int(input("please Enter your choice : "))
    if choice == 1:
        get_balance(name)
    elif choice == 2:
        temp = int(input("Please input amount to deposit : "))
        deposit_balance(temp)
    elif choice == 3:
        temp = int(input("Please input amount to withdraw : "))
        withdraw_amount(temp)
    elif choice == 4:
        print("Thank you")
        quit()
    elif choice == 1920:
        temp = int(input("Please input amount : "))
        set_balance(temp)
    else:
        print("Invalid choice, please choose again\n")
