# example 1

text = "  "
new_text = text.isspace()
print(new_text)

# Output : True

# example 2

text_1 = "\n\v"
new_text_1 = text_1.isspace()
print(new_text_1)

# Output : True

# example 3

text_2 = "   123   "
new_text_2 = text_2.isspace()
print(new_text_2)

# Output : False

# example 4

text_3 = "abcdef"
new_text_3 = text_3.isspace()
print(new_text_3)

# Output : False