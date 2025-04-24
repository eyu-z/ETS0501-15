# example 1

fruits = ['apple', 'banana', 'mango']

print(f"Original list: {fruits}")        # output:  Original list: ['apple', 'banana', 'mango']

fruits.clear()

print(f"List after clear(): {fruits}")   # output: List after clear(): []

# example 2

numbers = [1, 2, 3, 4, 5]

print(f"Before clearing: {numbers}")     # output: Before clearing: [1, 2, 3, 4, 5]

numbers.clear()

print(f"After clearing: {numbers}")      # output: After clearing: []

# example 3

empty_list = []

print(f"Initially: {empty_list}")        # output: Initially: []

empty_list.clear()

print(f"After clear(): {empty_list}")    # output: After clear(): []