# Example 1: Adding a single item using add()

my_set = {"apple", "banana"}

print(f"Initial set: {my_set}")

my_set.add("cherry")

print(f"Set after adding 'cherry': {my_set}")

my_set.add("banana")  # Adding a duplicate element has no effect

print(f"Set after adding 'banana' again: {my_set}")

# Example 2: Adding multiple items using update() with a list


my_set = {1, 2, 3}

print(f"\nInitial set: {my_set}")

new_elements_list = [3, 4, 5, 5]

my_set.update(new_elements_list)

print(f"Set after updating with a list: {my_set}")
# output: Initial set: {1, 2, 3} 
#         Set after updating with a list: {1, 2, 3, 4, 5}


# Example 4: Adding multiple items using update() with another set


set1 = {10, 20}

set2 = {20, 30, 40}

set1.update(set2)

print(f"Set1 after updating with set2: {set1}")
# output: Set1 after updating with set2: {20, 40, 10, 30}