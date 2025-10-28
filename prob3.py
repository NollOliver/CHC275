i = 0
word = input("What is your word?").strip().lower()
print(word)
check = True
while i < (len(word) - 1)//2 and check == True:
   
    if word[i] == word[len(word)- 1 - i]:
        i = i + 1
       
   
    else:
        check = False
       
if check == True:
    print("Congrats this is a palindrome")