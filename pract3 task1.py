# TASK 1 - All Patterns

n = 5

print("Pattern 1")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern 2")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

print("\nPattern 3")
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPattern 4")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")
    print()

print("\nPattern 5")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()

print("\nPattern 6")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()