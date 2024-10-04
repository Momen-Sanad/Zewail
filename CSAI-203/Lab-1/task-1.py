from abc import ABC, abstractmethod




class Account(ABC):



    def __init__(self):
        self._balance = 0

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit cant be 0 or less\n")
        else:
            self._balance += amount

    def get_balance(self):
        return float(self._balance)

    def subtract_balance(self, amount):
        self._balance -= amount

    @abstractmethod
    def withdraw(self, amount):
        pass




class SavingsAccount(Account):



    def __init__(self, _balance,rate=0.05):
        self.interest_rate = rate
        self._balance=_balance


    def calculate_interest(self):
        return self.get_balance() * self.interest_rate

    def withdraw(self, amount):
        raise NotImplementedError("Withdrawals are not allowed from savings account\n")




class CheckingAccount(Account):

    def __init__(self,_bal):
        self._balance=_bal


    def withdraw(self, amount):

        if(self.get_balance() >= amount):
            self.subtract_balance(amount)
            print("Balance withdrawn successfully\n")

        else:
            raise ValueError("Balance insufficient\n")


def main():


    #           TEST CASE 1
    savings_account = SavingsAccount(1000)

    print(f"Current saving account balance:{savings_account.get_balance()}\n")

    savings_account.deposit(500)
    print(f"Current saving account balance:{savings_account.get_balance()}\n")

    print(f"Current saving account rate of interest:{savings_account.calculate_interest()}\n")

    print("___________________________________________________________")

    #                  TEST CASE 2

    checking_account = CheckingAccount(500)
    print(f"Current checking account balance: {checking_account.get_balance()}\n")

    checking_account.deposit(200)
    print(f"Current checking account balance: {checking_account.get_balance()}\n")

    checking_account.withdraw(400)
    print(f"Current checking account balance: {checking_account.get_balance()}\n")

    try:
        checking_account.withdraw(500)

    except ValueError:
        print("Insufficient balance")

    print("___________________________________________________________")
    #                   TEST CASE 3


    savings_account2 = SavingsAccount(1000)

    try:
        savings_account2.withdraw(100)

    except NotImplementedError:
        print("Withdraw not allowed from savings account")


    print("___________________________________________________________")

        #           TEST CASE 4


    checking_account2 = CheckingAccount(500)

    try:

        checking_account2.deposit(-100)

    except ValueError:
        print("Deposit must be positive")


if __name__ == "__main__":
    main()
