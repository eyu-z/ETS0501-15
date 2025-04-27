# Example 1: Union using the | operator


set1 = {1, 2, 3}

set2 = {3, 4, 5}

union_set = set1 | set2

print(f"Set 1: {set1}")

print(f"Set 2: {set2}")

print(f"Union of set1 and set2 (| operator): {union_set}")
# output: Set 1: {1, 2, 3}
#         Set 2: {3, 4, 5}
#         Union of set1 and set2 (| operator): {1, 2, 3, 4, 5}

# Example 2: Union using the union() method

set3 = {"a", "b"}

set4 = {"b", "c", "d"}

union_set_method = set3.union(set4)

print(f"\nSet 3: {set3}")

print(f"Set 4: {set4}")

print(f"Union of set3 and set4 (union() method): {union_set_method}")
# output: Set 3: {'b', 'a'}
#         Set 4: {'c', 'b', 'd'}
#         Union of set3 and set4 (union() method): {'c', 'b', 'd', 'a'}

# Example 3: Update using the |= operator (in-place modification)

set8 = {100, 200}

set9 = {200, 300}

print(f"\nInitial Set 8: {set8}")

print(f"Set 9: {set9}")

set8 |= set9

print(f"Set 8 after update using |=: {set8}")  # set8 is now the union
# output: Initial Set 8: {200, 100}
#         Set 9: {200, 300}
#         Set 8 after update using |=: {200, 100, 300}

# Example 4: Update using the update() method (in-place modification)

set10 = {"x", "y"}

list_to_add = ["y", "z"]

print(f"\nInitial Set 10: {set10}")

print(f"List to add: {list_to_add}")

set10.update(list_to_add)

print(f"Set 10 after update using update(): {set10}")
# output: Initial Set 10: {'y', 'x'}
#         List to add: ['y', 'z']
#         Set 10 after update using update(): {'z', 'y', 'x'}