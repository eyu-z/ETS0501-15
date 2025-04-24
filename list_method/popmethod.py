# example 1

my_list = ['apple', 'banana', 'car', 'date']

removed_item = my_list.pop(1)  

print(f"Original list: {my_list}")          # output: ['apple', 'cherry', 'date']

print(f"Removed item: {removed_item}")      # output: 'banana'

# example 2

numbers = [10, 20, 30, 40, 50]

last_element = numbers.pop(4)  # Remove the element at index 4 (which is 50)

print(f"Updated list: {numbers}")   # output: [10, 20, 30, 40]

print(f"Last element removed: {last_element}")  # output:  50
# With negative index

negative_element = numbers.pop(-1)   # this will remove the last index(which is '20') 

print(negative_element)     # output: [10, 20, 30, 40] 