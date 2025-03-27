# example 1
text = "This method can checks if a string begins with a specified prefix. "

specified_text = text.startswith("can")

print(specified_text)
# the output will be False because can is on the index number 12

specified_text = text.startswith("can",12)
 
print(specified_text)
# now the output is True

# example 2

text = "Global warming is the most concering topic across the world."

specified_text = text.startswith("the",50)

print(specified_text)