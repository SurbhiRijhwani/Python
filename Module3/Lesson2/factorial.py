def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:\
        return x*factorial(x-1)

print(factorial.__doc__," : ",factorial(5))