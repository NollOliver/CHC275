print("welcome to calculator")


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. quit")

check = True
while check == True:

        math =input("enter your math:").strip().lower()
        try:
               
                if math == "addition":
                        x=input("num1:")
                        y=input("num2:")
                        x=int(x)
                        y=int(y)
                        sum=x+y
                        print(f"the sum of {x} + {y} = {sum}")
               
                elif math == "subtraction":
                        a=input("num3:")
                        b=input("num4:")
                        a=int(a)
                        b=int(b)
                        difference=a-b
                        print(f"the difference {a} - {b} = {difference}")
               
                elif math == "multiplication":
                        x=input("num1:")
                        y=input("num2:")
                        x=int(x)
                        y=int(y)
                        product=x*y
                        print(f"the product of {x} * {y} = {product}")
               
                elif math == "division":
                        a=input("num3:")
                        b=input("num4:")
                        a=int(a)
                        b=int(b)
                        quotient=a/b
                        print(f"the quotient {a} / {b} = {quotient}")

                elif math == "quit":
                        check = True
               
        except ValueError:
                print("x and y must be numbers")

        except ZeroDivisionError:
                print("y cannot be 0")

        except Exception as e:
                print(e)