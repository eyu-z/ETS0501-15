# Example 1: Using remove()


my_set = {10, 20, 30, 40}
print(f"Initial set: {my_set}")

my_set.remove(30)
print(f"Set after removing 30: {my_set}")

try:
    my_set.remove(50)  # Trying to remove an element that doesn't exist
except KeyError as e:
    print(f"Error: {e}")
# output: ERROR!
#             Initial set: {40, 10, 20, 30}
#             Set after removing 30: {40, 10, 20}
#             Error: 50

# Example 2: Using discard()


my_set = {"alpha", "beta", "gamma"}
print(f"\nInitial set: {my_set}")

my_set.discard("beta")
print(f"Set after discarding 'beta': {my_set}")

my_set.discard("delta")  # Discarding an element that doesn't exist (no error)
print(f"Set after discarding 'delta': {my_set}")
# output: Initial set: {'alpha', 'gamma', 'beta'}
#         Set after discarding 'beta': {'alpha', 'gamma'}
#         Set after discarding 'delta': {'alpha', 'gamma'}

# Example 3: Using pop()


my_set = {100, 200, 300}
print(f"\nInitial set: {my_set}")

removed_item = my_set.pop()
print(f"Removed item using pop(): {removed_item}")
print(f"Set after pop(): {my_set}")

empty_set = set()
try:
    empty_set.pop()  # Popping from an empty set
except KeyError as e:
    print(f"Error: {e}")

# Example 4: Using clear()


my_set = {"one", "two", "three"}
print(f"\nInitial set: {my_set}")

my_set.clear()
print(f"Set after clear(): {my_set}")