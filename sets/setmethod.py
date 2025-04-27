# example on add(element)

my_set = {1, 2, 3}
print(f"Initial set: {my_set}")
my_set.add(4)
print(f"Set after adding 4: {my_set}")
my_set.add(2)  # Adding a duplicate has no effect
print(f"Set after adding 2 again: {my_set}")

# example on update(iterable)

set1 = {10, 20}
my_list = [20, 30, 40]
my_tuple = (40, 50)
set2 = {50, 60}

set1.update(my_list)
print(f"Set1 after updating with a list: {set1}")
set1.update(my_tuple)
print(f"Set1 after further update with a tuple: {set1}")
set1.update(set2)
print(f"Set1 after updating with another set: {set1}")

# example on remove(element)

my_set = {"red", "green", "blue"}
print(f"Initial set: {my_set}")
my_set.remove("green")
print(f"Set after removing 'green': {my_set}")
try:
    my_set.remove("yellow")  # Element not in the set
except KeyError as e:
    print(f"Error: {e}")

# example on discard(element)

my_set = {1.1, 2.2, 3.3}
print(f"Initial set: {my_set}")
my_set.discard(2.2)
print(f"Set after discarding 2.2: {my_set}")
my_set.discard(4.4)  # Element not in the set, no error
print(f"Set after discarding 4.4: {my_set}")

# example on pop()

my_set = {"alpha", "beta", "gamma"}
print(f"Initial set: {my_set}")
removed_item = my_set.pop()
print(f"Removed item: {removed_item}")
print(f"Set after pop(): {my_set}")

empty_set = set()
try:
    empty_set.pop()
except KeyError as e:
    print(f"Error: {e}")

# example on clear()

my_set = {"one", "two", "three"}
print(f"Initial set: {my_set}")
my_set.clear()
print(f"Set after clear(): {my_set}")

# example on union(other_set, ...) or | operator

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6}

union_set1 = set_a.union(set_b)
print(f"Union of set_a and set_b (union()): {union_set1}")
union_set2 = set_a | set_b | set_c
print(f"Union of set_a, set_b, and set_c (| operator): {union_set2}")

# example on intersection(other_set, ...) or & operator

set_x = {10, 20, 30, 40}
set_y = {30, 40, 50}
set_z = {40, 60}

intersection_set1 = set_x.intersection(set_y)
print(f"Intersection of set_x and set_y (intersection()): {intersection_set1}")
intersection_set2 = set_x & set_y & set_z
print(f"Intersection of set_x, set_y, and set_z (& operator): {intersection_set2}")

# example on difference(other_set, ...) or - operator

set_p = {100, 200, 300, 400}
set_q = {300, 400, 500}
set_r = {400, 600}

difference_set1 = set_p.difference(set_q)
print(f"Difference of set_p and set_q (difference()): {difference_set1}")
difference_set2 = set_p - set_q - set_r
print(f"Difference of set_p, set_q, and set_r (- operator): {difference_set2}")

# example on symmetric_difference(other_set) or ^ operator

set_m = {"apple", "banana", "cherry"}
set_n = {"banana", "date"}

symmetric_difference_set = set_m.symmetric_difference(set_n)
print(f"Symmetric difference of set_m and set_n (symmetric_difference()): {symmetric_difference_set}")
symmetric_difference_set_operator = set_m ^ set_n
print(f"Symmetric difference of set_m and set_n (^ operator): {symmetric_difference_set_operator}")

# example on isdisjoint(other_set)

set_u = {1, 2}
set_v = {3, 4}
set_w = {2, 5}

print(f"Is set_u disjoint from set_v? {set_u.isdisjoint(set_v)}")
print(f"Is set_u disjoint from set_w? {set_u.isdisjoint(set_w)}")

# example on issubset(other_set) or <= operator

set_sub = {1, 2}
set_sup = {1, 2, 3}
set_other = {1, 4}

print(f"Is set_sub a subset of set_sup? {set_sub.issubset(set_sup)}")
print(f"Is set_sub a subset of set_other? {set_sub.issubset(set_other)}")
print(f"Is set_sub <= set_sup? {set_sub <= set_sup}")
print(f"Is set_sub <= set_other? {set_sub <= set_other}")

# example on issuperset(other_set) or >= operator

set_sup = {1, 2, 3}
set_sub = {1, 2}
set_other = {1, 4}

print(f"Is set_sup a superset of set_sub? {set_sup.issuperset(set_sub)}")
print(f"Is set_sup a superset of set_other? {set_sup.issuperset(set_other)}")
print(f"Is set_sup >= set_sub? {set_sup >= set_sub}")
print(f"Is set_sup >= set_other? {set_sup >= set_other}")