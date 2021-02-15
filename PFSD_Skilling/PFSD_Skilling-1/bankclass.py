class Bank:
    Balance = 10000

    def __init__(self, name, acno):
        self.name = name
        self.acno = acno

    def display(self):
        print(self.name, self.acno)


class IBAcc(Bank):
    def __init__(self, name, acno, cvv):
        super().__init__(name, acno)
        self.cvv = cvv

    def display(self):
        super().display()
        print(self.cvv)


class MBAcc(IBAcc):
    def __init__(self, name, acno, cvv, otp, IFSc):
        super().__init__(name, acno, cvv)
        self.otp = otp
        self.IFSc = IFSc

    def display(self):
        super().display()
        print(self.otp, self.IFSc)


customer = MBAcc("ANR", 12005486, 999, 1234, "HDFC4560")
customer.display()
print("Balance : ", customer.Balance)
