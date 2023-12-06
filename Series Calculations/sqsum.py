# Recommendation:
# The code calculates the sum of the squares of the first n odd natural numbers.
# It uses a loop to iterate through the odd numbers and accumulate their squares.

# Not recommended:
# The code is straightforward for its purpose. However, for better efficiency, consider using a formula to directly compute the sum.

# How to modify for a different value of n:
# Change the value of 'n' to the desired number of odd natural numbers.

# Improved code with informative output:

# Function that returns the sum of the squares of the first n odd natural numbers
def squaresum_odd(n):
    # Initialize the sum to 0
    sum_odd_squares = 0
    # Iterate i from 1 to n, checking if i is odd before adding its square to the sum
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if i is odd
            sum_odd_squares += i * i  # Calculate the square of i and add it to the sum
    return sum_odd_squares

# Main Program
# Specify the number of odd natural numbers, n
n = 20
# Call the function squaresum_odd
result = squaresum_odd(n)
# Print the result with informative output
print(f"The sum of the squares of the first {n} odd natural numbers is: {result}")
