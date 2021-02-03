balance = 0


def set_balance(amount):
    global balance
    balance = amount


def get_balance(name):
    print(name + " Your balance is ", balance, "\n")


def deposit_balance(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited Successfully remaining balance is ", balance)


def withdraw_amount(amount):
    global balance
    if amount > balance:
        print("Insufficient funds")
    else:
        balance = balance - amount
        print("Amount Withdrawn Successfully remaining balance is ", balance)
