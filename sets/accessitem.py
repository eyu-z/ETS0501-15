# Example 1: Checking for membership using the 'in' operator

my_set = {"apple", "banana", "cherry"}

if "apple" in my_set:
    print("Apple is in the set.")
else:
    print("Apple is not in the set.")

if "grape" in my_set:
    print("Grape is in the set.")
else:
    print("Grape is not in the set.")
# output: Apple is in the set.
#         Grape is not in the set.

# Example 2: Iterating through a set using a for loop

my_set = {10, 20, 30, 40, 50}

print("Elements in the set:")

for number in my_set:

    print(number)
# output: Elements in the set:
#         50
#         20
#         40
#         10
#         30