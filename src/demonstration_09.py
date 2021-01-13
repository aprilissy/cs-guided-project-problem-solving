"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
import math
def get_middle(input_str):
    each = list(input_str)
    input_len = len(each)
    mid = round(input_len / 2)
    if input_len % 2 == 0:
        return each[mid - 1] + each[mid]
    elif input_len % 2 != 0:
        return each[mid - 1]

print(get_middle("test")) # -> "es"
print(get_middle("testing")) # -> "t"
print(get_middle("middle")) # -> "dd"
print(get_middle("A")) # -> "A"
