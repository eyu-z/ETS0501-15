# example 1

text = "Password123"

new_text = text.isalnum()

print(new_text)

# Output : True

# example 2

text_2 = "password"

new_text_2 = text_2.isalnum()

print(new_text_2)

# Output : True

text_3 = "12345678"

new_text_3 = text_3.isalnum()

print(new_text_3)

# Output : True

text_4 = "password 123"

new_text_4 = text_4.isalnum()

print(new_text_4)

# Output : False