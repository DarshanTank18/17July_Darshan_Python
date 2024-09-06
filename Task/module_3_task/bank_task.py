# Bank task
import random

class Opening:
    def opening_data(self):
        self.acc_type = input("Enter account type: ")
        self.holder_name = input("Enter account holder name: ")

class Deposit:
    def deposit_data(self):
        self.amount = int(input("Enter deposit amount: "))
        while self.amount < 2000:
            print("Please deposit at least 2000.")
            self.amount = int(input("Re-enter your deposit amount: "))
        print("Amount deposited successfully.")
        return self.amount

class Withdrawal():
    def withdrawal_data(self):
        self.w_amount = int(input("Enter your withdrawal amount: "))
        while w_amount > self.amount:
            print("Insufficient balance...")
            w_amount = int(input("Re-enter your withdrawal amount: "))
        print("Amount withdrawn successfully.")
        return w_amount

class Statement(Opening, Deposit, Withdrawal):
    def statement_data(self):
        self.amount -= self.w_amount

        print("\nAccount Statement")
        print("===================")
        print("ID:", random.randint(0, 999999))
        print("Account type:", self.acc_type)
        print("Account holder name:", self.holder_name)
        print("Remaining balance:", self.amount)

st = Statement()
st.statement_data()
