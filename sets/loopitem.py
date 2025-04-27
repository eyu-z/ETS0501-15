# example

my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)
# output: banana
#         cherry
#         apple

# example 2

numbers = {1, 3, 5, 7, 9}

for num in numbers:
    squared_num = num ** 2
    
    print(f"The square of {num} is {squared_num}")
# output: The square of 1 is 1
#         The square of 3 is 9
#         The square of 5 is 25
#         The square of 7 is 49
#         The square of 9 is 81

# example 3

fruits = {"mango", "grape", "orange"}
search_fruit = "grape"

for fruit in fruits:
    if fruit == search_fruit:
        print(f"Found {search_fruit} in the set!")
        break  # Exit the loop once the item is found
else:
    print(f"{search_fruit} not found in the set.")
# output: Found grape in the set!