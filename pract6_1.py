# Practical 6 - Lab Assignment 1

text = input("Enter a string: ")

vowels = consonants = spaces = lowercase = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

    if ch == " ":
        spaces += 1

    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)