          # Using Curly Braces and Accessing Dictionary Items:

my_dict = {"name": "eyoel", "age": 20, "department": "electro"}

print(f"name: {my_dict['name']}")
print(f"age: {my_dict['age']}")
print(f"department: {product_info.get('department')}")
# output : name: eyoel
#          age: 20
#          department: electro

           # using the dict() constructor and Accessing Dictionary Items:

items = [("product", "Laptop"), ("price", 1200), ("color", "Silver")]

product_info = dict(items)

print(f"price: {product_info['price']}")

print(product_info.get('product'))
# output: price: 1200
#         Laptop

          # Modifying Dictionaries

# Initial dictionary
my_info = {"name": "eyoel", "age": 20, "department": "electro"}
print(f"Initial dictionary: {my_info['age']}")

# 1. Modifying an existing value
my_info["age"] = 21
print(f"After updating age: {my_info['age']}")

# output: Initial dictionary: 20
#         After updating age: 21

         # removing item

my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Initial dictionary: {my_dictionary}")

# 1. Removing a specific item using del keyword

del my_dictionary["b"]

print(f"After deleting key 'b': {my_dictionary}")