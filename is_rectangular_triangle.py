 ##Create function that will return true if from given parameters, trianglar triangle can be made of. In case you can't do that, function will return false.

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))


# Right triangle (90 degrees)
def is_rectangular_triangle(a,b,c):
    if a**2 + b**2 == c**2:
        print("This is right triangle")
    else:
        print("This is not right triangle")

    
# x = is_rectangular_triangle(a,b,c)


"""def is_triangle(a,b,c,):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("Trinagle cannot be formed")
    else: 
        print("Triangle can be formed")
is_triangle(a,b,c)"""
 