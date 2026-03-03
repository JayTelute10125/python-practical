# TASK 2 - All Patterns

n = 5

print("Pattern A")
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPattern B")
for i in range(1, n + 1):
    for j in range(i):
        print("#", end=" ")
    print()

print("\nPattern C")
for i in range(1, n + 1):
    ch = chr(64 + i)
    for j in range(i):
        print(ch, end="")
    print()

print("\nPattern D")
word = "python"
for i in range(1, len(word) + 1):
    for j in range(i):
        print(word[j], end="")
    print()