# Example 1: Sorting a list of numbers in ascending order (default)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()

print(numbers)             # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Example 2: Sorting a list of strings in alphabetical order (default)

fruits = ["banana", "apple", "orange", "grape"]

fruits.sort()

print(fruits)               # Output: ['apple', 'banana', 'grape', 'orange']

# Example 3: Sorting in descending order

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort(reverse=True)

print(numbers)              # Output: [9, 6, 5, 4, 3, 2, 1, 1]