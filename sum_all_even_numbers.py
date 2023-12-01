# Read an integer from input and assign it to 'target' (assumed to be between 0 and 1000)
target = int(input()) # Number between 0 and 1000

# Your code here 👇
even_sum = 0  # Initialize 'even_sum' to accumulate the sum of even numbers

# Iterate through the range starting from 2 to 'target' (inclusive), incrementing by 2 each time
for number in range(2, target + 1, 2):
    even_sum += number  # Add the current even number to 'even_sum'

# Output the final sum of even numbers up to 'target'
print(even_sum)  # Print the calculated sum of even numbers