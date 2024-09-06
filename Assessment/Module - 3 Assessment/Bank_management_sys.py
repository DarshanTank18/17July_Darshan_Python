"""def display_menu():
    print("\nWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
    print("Select your role")
    print("1) Banker")
    print("2) Customer")
    print("3) Exit\n")
    role = int(input("Enter your role: "))  # Ensuring role is returned as an integer
    return role

def banker():
    c_id = ""
    print("\nWelcome to Banker's App")
    print("Operation Menu")
    print("1) Add Customer")
    print("2) View Customer")
    print("3) Search Customer")
    print("4) View all customers")
    print("5) Total Amounts in Bank\n")
    
    banker_ope = int(input("Enter operation which you want to perform: "))
    
    if banker_ope == 1:
        add_customer()
    elif banker_ope == 2:
        print("ABC...")
    elif banker_ope == 3:
        print("Searching for a customer...")
    elif banker_ope == 4:
        print("Viewing all customers...")
    elif banker_ope == 5:
        print("Displaying total amounts in the bank...")
    else:
        print("Invalid operation. Please try again.")
    
def customer():
    print("\nWelcome to Customer's App")
    print("1) Withdraw Amount")
    print("2) Deposit Amount")
    print("3) View Balance")
    
    customer_ope = int(input("Enter operation which you want to perform: "))
    
    if customer_ope == 1:
        print("Withdrawing amount...")
    elif customer_ope == 2:
        print("Depositing amount...")
    elif customer_ope == 3:
        print("Viewing balance...")
    else:
        print("Invalid operation. Please try again.")

while True:
    choice = display_menu()

    if choice == 1:
        banker()
    elif choice == 2:
        customer()
    elif choice == 3:
        print("Exiting the system...")
        break
    else:
        print("Invalid option, please select a valid role.")

def add_customer():
    c_id = int(input("Enter 6 digit customer ID: "))
    c_name = input("Enter customer name: ")
    c_number = input("Enter customer phone number: ")
    c_amount = int(input("Enter initial deposit (min 2000): "))
    
    while c_amount < 2000:
        print("The initial deposit must be at least 2000.")
        c_amount = int(input("Re-enter initial deposit: "))

    customers[c_id] = {
        "name": c_name,
        "number": c_number,
        "balance": c_amount
    }
    
    print(f"Customer {c_name} added successfully!")"""

customers = {}

def display_menu():
    print("\nWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
    print("Select your role")
    print("1) Banker")
    print("2) Customer")
    print("3) Exit\n")
    role = int(input("Enter your role: "))  # Ensuring role is returned as an integer
    return role

def banker():
    print("\nWelcome to Banker's App")
    print("Operation Menu")
    print("1) Add Customer")
    print("2) View Customer")
    print("3) Search Customer")
    print("4) View all customers")
    print("5) Total Amounts in Bank\n")
    
    banker_ope = int(input("Enter operation which you want to perform: "))
    
    if banker_ope == 1:
        add_customer()
    elif banker_ope == 2:
        view_customer()
    elif banker_ope == 3:
        search_customer()
    elif banker_ope == 4:
        view_all_customers()
    elif banker_ope == 5:
        total_amount_in_bank()
    else:
        print("Invalid operation. Please try again.")
    
def add_customer():
    c_id = int(input("Enter 6 digit customer ID: "))
    c_name = input("Enter customer name: ")
    c_number = input("Enter customer phone number: ")
    c_amount = int(input("Enter initial deposit (min 2000): "))
    
    while c_amount < 2000:
        print("The initial deposit must be at least 2000.")
        c_amount = int(input("Re-enter initial deposit: "))

    customers[c_id] = {
        "name": c_name,
        "number": c_number,
        "balance": c_amount
    }
    
    print(f"Customer {c_name} added successfully!")

def view_customer():
    v_id = int(input("Enter customer ID to view details: "))
    
    if v_id in customers:
        print(f"Customer ID: {v_id}")
        print(f"Customer Name: {customers[v_id]['name']}")
        print(f"Customer Phone: {customers[v_id]['number']}")
        print(f"Total Balance: {customers[v_id]['balance']}")
    else:
        print("Customer not found.")

def search_customer():
    search_id = int(input("Enter customer ID to search: "))
    
    if search_id in customers:
        print(f"Customer {customers[search_id]['name']} found!")
    else:
        print("Customer not found.")

def view_all_customers():
    if customers:
        print("\nList of all customers:")
        for cid, details in customers.items():
            print(f"ID: {cid}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("No customers found.")

def total_amount_in_bank():
    total_amount = sum(customer['balance'] for customer in customers.values())
    print(f"Total amount in the bank: {total_amount}")

def customer():
    print("\nWelcome to Customer's App")
    print("1) Withdraw Amount")
    print("2) Deposit Amount")
    print("3) View Balance")
    
    customer_ope = int(input("Enter operation which you want to perform: "))
    
    if customer_ope == 1:
        withdraw_amount()
    elif customer_ope == 2:
        deposit_amount()
    elif customer_ope == 3:
        view_balance()
    else:
        print("Invalid operation. Please try again.")

def withdraw_amount():
    c_id = int(input("Enter your customer ID: "))
    if c_id in customers:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= customers[c_id]['balance']:
            customers[c_id]['balance'] -= withdraw
            print(f"Amount withdrawn: {withdraw}")
        else:
            print("Insufficient balance.")
    else:
        print("Customer ID not found.")

def deposit_amount():
    c_id = int(input("Enter your customer ID: "))
    if c_id in customers:
        deposit = int(input("Enter amount to deposit: "))
        customers[c_id]['balance'] += deposit
        print(f"Amount deposited: {deposit}")
    else:
        print("Customer ID not found.")

def view_balance():
    c_id = int(input("Enter your customer ID: "))
    if c_id in customers:
        print(f"Your current balance is: {customers[c_id]['balance']}")
    else:
        print("Customer ID not found.")

# Main Loop
while True:
    choice = display_menu()

    if choice == 1:
        banker()
    elif choice == 2:
        customer()
    elif choice == 3:
        print("Exiting the system...")
        break
    else:
        print("Invalid option, please select a valid role.")
