small = []
medium = []
large = []

check = False
while check == False:
   
    option = input("What is the size of your mushroom?").strip().lower()
    print(option)

    if option == "stop":
            check = True
           
    if option.isnumeric():
        option = int(option)
       
    if option <= 100:
        small.append
        print("You have a small Mushroom")
       
    elif option > 100 and option < 200:
        medium.append
        print("You have a medium Mushroom")
           
    elif option >= 200:
        large.append
        print("You have a large Mushroom")
           
    else:
        print("That is not a number!")

