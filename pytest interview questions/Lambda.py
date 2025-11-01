# Lambda functions are anonymous functions that contain only one expression.
# They are useful for short, simple operations.
# Avoid using lambda when multiple expressions or complex logic are required.

# Regular function definition
def add(x, y):
    return x + y

# The same logic written using a lambda function
add = lambda x, y: x + y  # single-line function that adds two numbers


# ✅ Using lambda with map()
# The map() function applies the given lambda function to each element in the list.
list_numbers = [1, 2, 3, 4]  # List of numbers

# Multiply each number by 2 using map and lambda
squared_numbers = map(lambda x: x * 2, list_numbers)

# Convert map object to a list and print it
print(list(squared_numbers))  # Output: [2, 4, 6, 8]


# ✅ Using lambda with filter()
# The filter() function filters elements based on a condition provided by the lambda.
numbers = [1, 2, 3, 4]  # List of numbers

# Keep only even numbers using filter and lambda
filtered_even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert filter object to a list and print it
print(list(filtered_even_numbers))  # Output: [2, 4]


# ✅ Without using lambda (using a for loop)
# This is the longer, traditional way to multiply numbers by 2.
listed_numbers = [1, 2, 3, 4]
squared_numbers = []

for i in listed_numbers:
    squared_numbers.append(i * 2)

print(squared_numbers)  # Output: [2, 4, 6, 8]
