# Practical 5 - Lab Assignment 1

nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total items:", len(nums))

# b) Last item
print("Last item:", nums[-1])

# c) Elements in reverse order
print("Reverse order:", nums[::-1])

# d) Check if 5 exists
if 5 in nums:
    print("Yes, 5 exists in the tuple")
else:
    print("No, 5 does not exist")

# e) Remove first and last item, sort remaining
if len(nums) > 2:
    new_tuple = tuple(sorted(nums[1:-1]))
    print("After removing first & last and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last")