

n = int(input("Enter a positive integer: "))

if n <= 1:
    print(n, "is not a Prime number")
else:
    is_prime = True
    for i in range(2, n): 
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a Prime number")
    else:
        print(n, "is not a Prime number")
