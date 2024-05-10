# this is the method that is used to remove leading and trailling whitespace in the string
#of word, its syntac is strip()
text = "  Hello, world!  "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, world!"

text = "\nHello, world!\n"
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, world!"

empty_text = ""
stripped_text = empty_text.strip()
print(stripped_text)  # Output: ""

text = """
    Hello, 
    world!
"""
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello,\nworld!"
