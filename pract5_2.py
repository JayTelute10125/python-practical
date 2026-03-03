# Practical 5 - Lab Assignment 2

prices = tuple(map(float, input("Enter item prices separated by space: ").split()))

# a) Total number of items
print("Total items sold:", len(prices))

# b) Cheapest item
print("Cheapest item price:", min(prices))

# c) Costliest item
costliest = max(prices)
print("Costliest item price:", costliest)

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
print("Number of costliest items sold:", prices.count(costliest))