def opening():
    acc_no = input("Enter account number: ")
    acc_type = input("Enter account type: ")
    holder_name = input("Enter account holder name: ")

    return acc_no, acc_type, holder_name

def deposit():
    amount = int(input("Enter deposit amount: "))
    while amount < 2000:
        print("Please deposit at least 2000.")
        amount = int(input("Re-enter your deposit amount: "))
    
    print("Amount deposited successfully.")
    return amount

def withdrawal(balance):
    w_amount = int(input("Enter your withdrawal amount: "))
    while w_amount > balance:
        print("Insufficient amount...")
        print("Your balance is", balance)
        w_amount = int(input("Re-enter your withdrawal amount: "))
    
    print("Amount withdrawn successfully.")
    return w_amount

def statement():
    acc_details = opening()
    balance = deposit()
    w_amount = withdrawal(balance)

    print("\nAccount Statement")
    print("===================")
    print("Account number:", acc_details[0])
    print("Account type:", acc_details[1])
    print("Account holder name:", acc_details[2])
    balance -= w_amount
    print("Remaining balance:", balance)

statement()
