text = "This method can checks if a string ends with a specified prefix."

ending_text= text.endswith("prefix.")

print(ending_text)

# the output is True 
 
text_2 = "This method can checks if a string ends with a specified prefix."

ending_text_2 = text_2.endswith("checks",0,16)

print(ending_text_2)