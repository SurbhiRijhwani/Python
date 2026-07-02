num = int(input("Enter a number: "))
count = 0
rev = 0
while num > 0:
    rev = rev*10 + num%10
    count+=1
    num//=10
print("The reverse of the number is: ", rev)
print("The number of digits in the number is: ", count)