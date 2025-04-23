# example 1

fruits = ["apple", "banana", "mango"]

print(fruits)
# output : ['apple', 'banana', 'mango']

fruits.append("orange")

print(fruits)
# output : ['apple', 'banana', 'cherry', 'orange']

# example 2 (With Different Data Types)

my_list = [10, "hello", 3.14]

print(my_list)
# output : [10, 'hello', 3.14]

my_list.append(True)
my_list.append([1, 2, 3])
my_list.append(("a", "b"))

print(my_list)
# output : [10, 'hello', 3.14, True, [1, 2, 3], ('a', 'b')]

# example 3 (in a Loop)

squares = []
for i in range(5):
    square = i * i
    squares.append(square)

print(squares)
# output : [0, 1, 4, 9, 16]