# startswithmethod

The startswith() method is a string method that checks if a string begins with a specified prefix. It returns True if the string starts with the prefix, and False otherwise.

string: The string you want to check.
prefix: The prefix you're looking for. This can be a string or a tuple of strings.
start (optional): The starting position within the string where the search begins.
end (optional): The ending position within the string where the search ends.

It's frequently used to filter data based on specific prefixes. For example, you might filter a list of filenames to find those that start with "report_" or "image_".
It simplifies the process of parsing strings by allowing you to quickly check for specific starting patterns.
It becomes very useful in conditional statements. For example, you may want to execute a section of code only if a string begins with certian characters.

# endswithmethod

The endswith() method is a string method that checks if a string ends with a specified suffix. It returns True if the string ends with the suffix, and False otherwise.

string: The string you want to check.
suffix: The suffix you're looking for. This can be a string or a tuple of strings.
start (optional): The starting position within the string where the search begins.
end (optional): The ending position within the string where the search ends.

A very common use case is to determine the type of a file based on its extension.
You can use endswith() to validate data formats.
When parsing text data, endswith() can help identify specific patterns at the end of lines or strings. This is useful for analyzing log files, configuration files, or other text-based data.

# countmethod

The count() method returns the number of occurrences of a specified substring within a string.

substring: (Required) The substring you want to count.
start: (Optional) The index where the search begins. The default is 0.
end: (Optional) The index where the search ends. The default is the end of the string.
The count() method returns an integer representing the number of times the substring appears.

Case-sensitive: The count() method is case-sensitive. "A" and "a" are considered different.
It counts non-overlapping occurences.
It's versatile for string analysis.

# replacemethod

The replace() method is a fundamental string manipulation tool found in many programming languages, including Python and Java. Its primary function is to substitute occurrences of a specified substring within a string with another substring.
The replace() method creates a new string where designated parts of the original string are replaced.
It does not modify the original string itself; strings are typically immutable.
old: The substring to be replaced.
new: The substring to replace old with.
count (optional): The maximum number of replacements to make.

The replace() method is generally case-sensitive. "Hello" and "hello" are treated as distinct substrings.
The method returns a new string with the replacements applied.

# stripmethod

 The strip() method is a powerful tool for cleaning up strings by removing unwanted characters from their beginning and end.
 The primary purpose of strip() is to eliminate leading and trailing characters from a string.
By default, it removes whitespace characters, including spaces, tabs (\t), and newlines (\n).
It can also be customized to remove specific characters.

string: The string you want to modify.
[characters] (optional): A string specifying the characters to remove. If omitted, whitespace is removed.

Removes from both ends: strip() affects both the beginning and end of the string.
Does not modify the original string: It returns a new string with the specified characters removed.

Character removal: If you provide a characters argument, strip() removes any characters from the beginning and end of the string that are present in that argument. The order of characters in the characters argument doesn't matter.

The strip() method is very useful for cleaning up user input, data retrieved from files, or any other strings that may contain unwanted leading or trailing characters.

# lstripmethod

The str.lstrip() method is used to remove leading characters from a string. "Leading" means the characters at the beginning (left side) of the string.

str.lstrip() creates a new string by removing characters from the left side of the original string.
By default, if no characters are specified, it removes leading whitespace characters (spaces, tabs, newlines).
If you provide a string of characters as an argument, it removes any of those characters that appear at the beginning of the string.
It stops removing characters as soon as it encounters a character that is not in the specified set.
It does not modify the original string; it returns a new, modified string.
    The key difference between strip and lstrip is :-
strip() removes characters from both ends of the string.
lstrip() removes characters only from the left (beginning) of the string.

# rstripmethod

The str.rstrip() method is used to remove trailing characters from a string. "Trailing" means the characters at the end (right side) of the string.

str.rstrip() creates a new string by removing characters from the right side of the original string.
By default, if no characters are specified, it removes trailing whitespace characters (spaces, tabs, newlines).
If you provide a string of characters as an argument, it removes any of those characters that appear at the end of the string.
It stops removing characters as soon as it encounters a character that is not in the specified set.
It does not modify the original string; it returns a new, modified string.
        key differences 
strip() removes characters from both ends of the string.
lstrip() removes characters only from the left (beginning) of the string.
rstrip() removes characters only from the right (end) of the string.

# splitmethod

The str.split() method is used to break a string into a list of substrings based on a specified delimiter.
str.split() returns a list of strings, where each element in the list is a substring from the original string.
If no delimiter is provided, it splits the string by whitespace (spaces, tabs, newlines) by default.
If a delimiter is provided, it splits the string wherever that delimiter occurs.
Consecutive delimiters are treated as separate splits, resulting in empty strings in the list.
The delimiter itself is not included in the resulting list.

str: The string you want to split.
[separator] (optional): The delimiter string. If omitted, whitespace is used.
[maxsplit] (optional): An integer specifying the maximum number of splits to perform. If omitted or -1, all possible splits are made.

The str.split() method is very useful for parsing strings, extracting information, and breaking down text into manageable chunks.