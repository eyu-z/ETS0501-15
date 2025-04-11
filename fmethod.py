# example 1

name = "Basha"
age = 25
city = "Adama"

# Embedding variables directly

message1 = f"My name is {name}, I am {age} years old, and I live in {city}."

print(message1)

# Output: My name is Basha, I am 25 years old, and I live in Adama.

# Embedding expressions

next_year_age = age + 1

message2 = f"Next year, I will be {next_year_age} years old."

print(message2)

# Output: Next year, I will be 26 years old.


def greet(person_name):

  return f"Hello, {person_name}!"

greeting = f"{greet(name)}"

print(greeting)

# Output: Hello, Basha!
