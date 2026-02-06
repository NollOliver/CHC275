def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y
    
def multiply(x,y): 
    return x * y

def divide(x,y):
    return x / y

def pow(x,y):
    return x**y

def main():
    print("Welcome to the calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power ")
    check = True
    while check == True:
        option = input("Select your operation or type quit to exit: ")
        if option == "1":
           
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                
                sum = add(num1,num2)
                print(f"your sum is: {sum}")
                
        if option == "2":
           
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                
                sum = subtract(num1,num2)
                print(f"your difference is: {sum}")
                
        if option == "3":
            
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                
                sum = multiply(num1,num2)
                print(f"your product is: {sum}")
                
        if option == "4":
            
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                
                sum = divide(num1,num2)
                print(f"your quotient is: {sum}")
                
        if option == "5":
           
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                
                sum = pow(num1,num2)
                print(f"your result is: {sum}")
        
            
        if option == "quit":
            check = False
            
if __name__ == "__main__": 
    main()