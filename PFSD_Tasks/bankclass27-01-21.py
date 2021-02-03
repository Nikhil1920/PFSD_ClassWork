class bank(object):
    def __init__(self, accnumin, namein, balancein, bankin):
        self.accountnumber = accnumin
        self.name = namein
        self.balance = balancein
        self.bankname = bankin

    def get_balance(self):
        print("Current balance in your account is : " + str(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(amount, "Withdrew Succesfully\n remaining balance = " +
                  str(self.balance))

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(amount, "Deposited Succesfully\n remaining balance = " +
              str(self.balance))

    def enquiry(self):
        enquiryoutput = f'''
        Account Number : {self.accountnumber}
        Account Holder Name : {self.name}
        Current Balance : {self.balance}
        Bank Name : {self.bankname}
        '''
        print(enquiryoutput)


class internetBank(bank):
    print("")
    pass


class MobileBank(bank):
    pass


accnumin = int(
    input("Welcome to HDFC Bank\n please enter your account number to continue \n"))

namein = input("Please enter the account holder's name \n")

bankobj = bank(accnumin, namein, 200000, "HDFC Bank")

print("Loggedin Succesfully\n Welcome Mr. " + namein +
      "\n now you can use the menu for banking services")

print
while True:
    print("\nMenu\n(1)View Balance\n(2)Deposit amount\n(3)Withdraw amount\n(4)Quit")
    choice = int(input("please Enter your choice : "))
    if choice == 1:
        bankobj.get_balance()
    elif choice == 2:
        temp = int(input("Please input amount to deposit : "))
        bankobj.deposit(temp)
    elif choice == 3:
        temp = int(input("Please input amount to withdraw : "))
        bankobj.withdraw(temp)
    elif choice == 4:
        print("Thank you")
        quit()
    else:
        print("Invalid choice, please choose again\n")
