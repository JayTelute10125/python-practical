# TASK 3: Print numbers from 1 to n

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i, end=" ")
print()


# TASK 4: Create a number from 1 to n (e.g., n=5 -> 12345)

n = int(input("Enter a number: "))

result = 0
for i in range(1, n + 1):
    result = result * 10 + i

print(result)


# TASK 5: Print pyramid pattern

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()


# TASK 6: Print diamond pattern

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# TASK 7: Print prime numbers between start and end

while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    
    if start < end and start >= 0:
        break
    else:
        print("Invalid input. Start must be less than End and non-negative.")

print("\nPrime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
print()
