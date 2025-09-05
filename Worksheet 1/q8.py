a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, " b =", b)
a, b = b, a
a = a + 1
print("After swapping and incrementing a: a =", a, " b =", b)