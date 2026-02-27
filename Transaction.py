#List based Transactions
balance = 0
transactions = []
while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Transaction History")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        transactions.append("Depoited: " + str(amount))
        print("Amount Deposited")
        
    elif choice == '2':
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            transactions.append("Withdrew: " + str(amount))
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")
            
    elif choice == '3':
        print("Current Balance: " + str(balance))
        
    elif choice == '4':
        print("Transaction History:")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)
    elif choice == '5':
        print("Exiting...")
        break
