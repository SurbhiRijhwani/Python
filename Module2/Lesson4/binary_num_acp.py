num = int(input("Enter a number: "))
res = ""
while num > 0:
    res = str(num%2) + res
    num//=2
print("The binary representation is: ", res)