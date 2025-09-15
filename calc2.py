print("welcome to the calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = input ("Chose your operation") 
if option== "addition":
    x = input("num1")
y = input("num2")
x = int(x) 
y = int(y) 
sum = x + y 
print(f"the sum of {x} + {y} = {sum}")
elif option== "subtraction":
w = input("num3") 
e = input("num4")
w = int(w) 
e = int(e) 
difference = w - e 
print(f"the difference of {w} - {e} = {difference}")
elif option== "multiplication":
x = input("num1")
y = input("num2")
x = int(x) 
y = int(y) 
product = x * y 
print(f"the product of {x} * {y} = {product}")
elif option== "division":
w = input("num3") 
e = input("num4")
w = int(w) 
e = int(e) 
quotient = w / e 
print(f"the quotient of {w} / {e} = {quotient}")
