# Program to check if three angles can form a triangle

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("The angles can form a triangle")
else:
    print("The angles cannot form a triangle")
