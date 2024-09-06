import random
class openacc():
    def opendata(self):
        self.acc_type = input("Enter acc type : ")
        self.holder_name = input("Enter account name : ")

class Deposit():
    def Depositdata(self):
        self.d_amount = int(input("Enter deposite amount : "))
        while self.d_amount < 2000 :
            print("Please deposit at least 2000.")
        print("Amount deposite successfully...")

class withdraw(Deposit):
    def withdrawdata(self):
        self.w_amount = int(input("Enter withdraw amount : "))
        while self.w_amount > self.d_amount :
            print("Insufficient balance...")
        print("Amount withdraw successfully...")

class statement(openacc,withdraw):
    def statementdata(self):
        self.d_amount -= self.w_amount

        print("id : ",random.randint(0,999999))
        print("Account type:", self.acc_type)
        print("Account holder name:", self.holder_name)
        print("Remaining balance:", self.d_amount)

st = statement()
st.opendata()
st.Depositdata()
st.withdrawdata()
st.statementdata()