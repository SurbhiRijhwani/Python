char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    code = ord(char)
    print(f"The ASCII value of '{char}' is {code}.")
    