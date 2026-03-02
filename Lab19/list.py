numbers = [1,2,3,4,5,6,7,8,9,10]
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Doubled Numbers:", doubled_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

from functools import reduce

# Use reduce with a lambda function to sum the numbers
total_sum = reduce(lambda x, y: x + y, numbers)

# Print the result
print("Sum of Numbers:", total_sum)
