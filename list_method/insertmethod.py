# example 1

colors = ["red", "green", "blue"]

colors.insert(1, "yellow")
# output : ['red', 'yellow', 'green', 'blue']

# example 2

numbers = [1, 3, 4]

print(numbers)      # output : [1, 3, 4]

# Insert at the beginning (index 0)
numbers.insert(0, 0)

print(numbers)      # output : [0, 1, 3, 4]

# Insert at an index beyond the current end
numbers.insert(len(numbers), 5) 
# len(numbers) gives the current length, which is the position after the last element

print(numbers)       # output : [0, 1, 3, 4, 5]