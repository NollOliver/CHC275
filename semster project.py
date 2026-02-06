
    print("Please restart the program to enter your details again.")
    money = input("Enter the amount of money you are willing to spend: ")
money = float(money)
if money < 10:
    print("You can not afford to go on a trip.")
elif money >= 10 and money < 100:age = inpuit("Enter your age: ")
gender = input("Enter your gender: ")
print(f"You are {age} years old and your gender is {gender}.")      
confirmation = input("Is this correct? (yes/no): ").strip().lower()
if confirmation == "yes":
    print("Thank you for confirming your details.") 
else:
    print("You ca go on a local trip.")
elif money >= 100 and money < 1000:
    print("You can go on a domestic trip.")
elif money >= 1000:
    print("You can go on an international trip.")
destination = input("Enter your desired travel destination: ")
print(f"You have chosen to travel to {destination}. Enjoy your trip!")
list_of_activities = []
while True:
    activity = input("Enter an activity you would like to do at your destination (or type 'done' to finish): ").strip()
    if activity.lower() == 'done':
        break
    list_of_activities.append(activity)
print("Here are the activities you have plannend for your trip:")
for idx, act in enumerate(list_of_activities, start=1):

    
    
