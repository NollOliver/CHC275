x =input ("Enter a positive integer: ")
x = int(x)
if x <= 0:
    print("Please enter a positive integer greater than 0.")
else:   
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2 
        elif x % 2 == 1: 
            x = 3 * x + 1 
        

