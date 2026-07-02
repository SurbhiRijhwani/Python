# Program to check whether the entered character is an alphabet or not.

char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        print(char,"is an alphabet.")
    else:
        print(char,"is not an alphabet.")
