# example 1
text = "Python is a popular programming language. Python is very powerful and it is simply understandable languge."

count_is = text.count("is")

print(count_is)

# The output will be 3.becuase there is no specification,it counts "is" from all sentences.

# example 2
text = "Python is a popular programming language. Python is very powerful and it is simply understandable languge."

count_is_2 = text.count("is",10)
print(count_is_2)

# Now the output is 2.becuase counting starts from index number 10.

# example 3
text = "This example checks the repitation of letters in a sentence."

count_a = text.count("a")

print(count_a)

#The output is 3.from the entire sentece.

text = "This example checks the repitation of letters in a sentence."

count_e = text.count("e",15)

print(count_e)
# The output is 8 which is after the index number 15.