"""
Name: Oliver Noll
Section:
Description: Lab 4
"""

import math
print("STATISTICS CALCULATOR--LAB 4")
def getList(userlist):
    userlist = []
    while True:
        user_input = input("Enter open to open the calculator: ")
        if user_input.lower() == 'open':
            break
        try:
            number = float(user_input)
            userlist.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'open'.")
    return userlist
"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied
"""


"""
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("1. Mean")
    print("2. Median")
    print("3. Minimum")
    print("4. Maximum")
    print("5. Standard Deviation")
    print("6. Exit")

"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value
"""
def getMean(userList):
    total = sum(userList)
    mean = total / len(userList)
    return mean

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)
    n = len(userList)
    mid = n // 2
    if n % 2 == 0:
        median = (userList[mid - 1] + userList[mid]) / 2
    else:
        median = userList[mid]
    return median

"""
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    min_value = min(userList)
    return min_value

"""
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    max_value = max(userList)
    return max_value

"""
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    mean = getMean(userList)
    variance = sum((x - mean) ** 2 for x in userList) / len(userList)
    stddev = math.sqrt(variance)
    return stddev




def main():
    userList = getList([])
    printMenu()
    choice = int(input("Enter your choice (1-6): "))

    while choice != 6:
        if choice == 1:
            userlist = [1,2,3,4,5,6,7,8,9,10]
            print(userList)
            input(f"enter list of numbers: {userList}")
            print(f"length of list: {len(userList)}")
            mean = getMean(userList)
            print(f"The mean is: {mean}")
        elif choice == 2:
            userlist = [1,2,3,4,5,6,7,8,9,10]
            input(f"enter list of numbers: {userList}")
            print(userList)
            print(f"length of list: {len(userList)}")
            median = getMedian(userList)
            print(f"The median is: {median}")
        elif choice == 3:
            userlist = [1,2,3,4,5,6,7,8,9,10]
            input(f"enter list of numbers: {userList}")
            print(userList)
            print(f"length of list: {len(userList)}")
            minimum = getMin(userList)
            print(f"The minimum is: {minimum}")
        elif choice == 4:
            userlist = [1,2,3,4,5,6,7,8,9,10]
            input(f"enter list of numbers: {userList}")
            print(userList)
            print(f"length of list: {len(userList)}")
            maximum = getMax(userList)
            print(f"The maximum is: {maximum}")
        elif choice == 5:
            userlist = [1,2,3,4,5,6,7,8,9,10]
            input(f"enter list of numbers: {userList}")
            print(userList)
            print(f"length of list: {len(userList)}")
            stddev = getStdDev(userList)
            print(f"The standard deviation is: {stddev}")
        else:
            print("Invalid choice. Please try again.")
       
        printMenu()
        choice = int(input("Enter your choice (1-6): "))
       

if __name__ == "__main__":
    main()
