# example 1

my_string = "你好，世界！"  # Contains non-ASCII characters

# Encode using the default 'utf-8' encoding

utf8_bytes = my_string.encode('utf-8')

print(f"UTF-8 encoded: {utf8_bytes}")

# Output (will be a bytes literal): UTF-8 encoded: b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# example 2

# Encode using 'latin-1' encoding (can handle a wider range of characters)

latin1_bytes = my_string.encode('latin-1')

print(f"Latin-1 encoded: {latin1_bytes}")

# Output (will show byte representations, possibly not directly readable): Latin-1 encoded: b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'
