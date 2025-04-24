# example 1

my_list = ['apple', 'banana', 'mango', 'banana']

index_of_banana = my_list.index('banana')

print(f"The first occurrence of 'banana' is at index: {index_of_banana}")   
 # output: The first occurrence of 'banana' is at index: 1

index_of_the_other_banana = my_list.index('banana',2)

print(f"the other banana occurrence is at index: {index_of_the_other_banana}")
 # output: the other banana occurrence is at index: 3

 # example 2

numbers = [10, 20, 30, 20, 40, 20, 50]

index_in_range = numbers.index(20, 1, 5)  # Search for 20 between index 1 (inclusive) and 5 (exclusive)

print(f"The first 20 found between index 1 and 4 is at index: {index_in_range}")
# output: The first 20 found between index 1 and 4 is at index: 3