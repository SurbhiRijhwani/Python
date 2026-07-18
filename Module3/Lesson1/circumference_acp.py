def circumference(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    return circumference

radius = float(input("Enter the radius of the circle: "))
result = circumference(radius)
print("The circumference of the circle is:", result)