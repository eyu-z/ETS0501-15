                    # Python dictionaries

Dictionaries in Python are unordered collections of data values, used to store data in key:value pairs.

Unordered (in Python < 3.7): Before Python 3.7, dictionaries did not guarantee any specific order of items. The order in which you added items might not be the order in which they are stored or retrieved.
Ordered (in Python 3.7+): Starting with Python 3.7, dictionaries remember the order in which items were inserted. This behavior became part of the language specification in Python 3.7.
Keys are Unique: Each key within a dictionary must be unique. If you try to add a new key that already exists, the old value associated with that key will be overwritten.
Keys are Immutable: Keys must be of an immutable data type, such as strings, numbers (integers, floats), and tuples (if they contain only immutable elements). Lists and other dictionaries cannot be used as keys because they are mutable.
Values can be of any type: The values associated with keys can be of any Python data type (strings, numbers, lists, tuples, other dictionaries, etc.).
Mutable: Dictionaries are mutable, meaning you can add, remove, and modify items after the dictionary is created.
Enclosed in Curly Braces {}: Dictionaries are defined using curly braces, with key-value pairs separated by colons : and items separated by commas ,.

Explanation of the Modifications:

Modifying an Existing Value:

You can change the value associated with an existing key by assigning a new value to it using square bracket notation (my_info["age"] = 21).
Adding a New Key-Value Pair:

To add a new key-value pair, simply assign a value to a new key using square bracket notation (my_info["product"] = "Engineer"). If the key doesn't exist, it will be added to the dictionary.
Using update():

The update() method allows you to merge another dictionary or an iterable of key-value pairs into the existing dictionary.
If a key in the updating dictionary already exists in the original dictionary, its value will be updated.
If a key in the updating dictionary does not exist in the original dictionary, it will be added.
Adding with update() (single item):

You can also use update() with a dictionary containing a single key-value pair to add a new item.
Removing a Key-Value Pair using del:

The del keyword is used to remove a specific key-value pair from the dictionary. You need to specify the key you want to remove (del my_info["age"]). If the key doesn't exist, it will raise a KeyError.
Removing and Returning a Value using pop():

The pop() method removes the key-value pair with the specified key and returns the corresponding value. If the key is not found, it raises a KeyError (unless you provide a default value as a second argument).
Removing the Last Inserted Item using popitem():

The popitem() method removes and returns the last inserted key-value pair as a tuple (key, value). In Python versions 3.7 and later, dictionaries maintain insertion order, so this will be the last item added. In older versions, the behavior might be unpredictable.
Accessing with get():

The get() method provides a safer way to access dictionary values. If the key exists, it returns the corresponding value. If the key doesn't exist, it returns None (or a default value you provide as the second argument), preventing a KeyError.
Checking Key Existence using in:

The in operator allows you to check if a specific key exists in the dictionary. It returns True if the key is present and False otherwise. This is useful for avoiding KeyError when trying to access or modify a key.