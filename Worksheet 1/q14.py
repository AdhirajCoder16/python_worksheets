n = int(input("Enter a positive integer: "))

if n <= 1:
    print(n, "is not a Prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1): 
            is_prime = False
            break

    if is_prime:
        print(n, "is a Prime number")
    else:
        print(n, "is not a Prime number")