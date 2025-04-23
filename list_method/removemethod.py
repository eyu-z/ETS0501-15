# example 1

fruits = ["apple", "banana", "cherry", "banana"]

print(fruits)         # output : ['apple', 'banana', 'cherry', 'banana']

fruits.remove("banana")

print(fruits)          # output : ['apple', 'cherry', 'banana']

# example 2

mixed_list = [10, "hello", 3.14, True, "hello"]

print(mixed_list)          # output : [10, 'hello', 3.14, True, 'hello']

mixed_list.remove("hello")

print(mixed_list)          # output : [10, 3.14, True, 'hello']

mixed_list.remove(True)

print(mixed_list)          # output : [10, 3.14, 'hello']