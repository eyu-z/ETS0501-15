# Example 1: Counting a specific number

numbers = [1, 2, 2, 3, 2, 4, 5]

count_of_2 = numbers.count(2)

print(f"The number 2 appears {count_of_2} times in the list.")
# output: The number 2 appears 3 times in the list.

# example 2

fruits = ["apple", "banana", "orange", "apple", "grape", "apple"]

count_of_apple = fruits.count("apple")

print(f"The string 'apple' appears {count_of_apple} times in the list.")
# output: The string 'apple' appears 3 times in the list.

# example 3

colors = ["red", "green", "blue"]

count_of_yellow = colors.count("yellow")

print(f"The string 'yellow' appears {count_of_yellow} times in the list.")
# outout: The string 'yellow' appears 0 times in the list.