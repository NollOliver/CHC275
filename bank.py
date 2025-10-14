actnames = ["Oliver"]
actbalances = [1,000]
check = False
while check == False:
        print("Welcome to First Financial Credit Union!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. List All Accounts")
        print("5. Add Account")
        print("6. Remove Account")
        action = input("What would you like to do today?:")
        if action == "Deposit":
            actname = input("Which account would like to Deposit into?:")
            money = input("how much would you like to Deposit?:")
            money= int(money)
            index= actnames.index(actname)
            actbalances[index] = actbalances[index] + money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
        elif action == "Withdraw":
            actname = input("Which account would like to Withdraw from?:")
            money = input("How much would you like to Withdraw?:")
            money= int(money)
            index= actnames.index(actname)
            actbalances[index] = actbalances[index] - money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
        elif action == "Transfer":
            actname = input("Which account would like to Transfer from?:")
            actname2 = input("Which account would like to Transfer to?:")
            money = input("how much would you like to Transfer?:")
            money= int(money)
            index= actnames.index(actname)
            index2 = actnames.index(actname2)
            actbalances[index] = actbalances[index] - money
            actbalances[index2] = actbalances[index2] + money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
        elif action == "List All Accounts":
            print(actnames)
        elif action == "Add Account":
            pass
        elif action == "Remove Account":
            print("option 3")
        elif action == "quit":
            check = True
for i in range(len(actnames)):
    print (f"Bank records for {actnames[i]}, actbalance: {actbalance[i]}")
