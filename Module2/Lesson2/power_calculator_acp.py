num = int(input("Enter a number: "))
power = int(input("Enter the power: "))
result = 1
for i in range(power):
    result *= num
print(num,"raised to the power of ",power," is ",result)