"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    print(*map(input_str.lower().count, 'aeiou'))
    vowels = 0
    for each in input_str:
        if each in 'aeiouAEIOU':
            vowels += 1
    return vowels

print(get_count('hello My name is April')) # 7
print(get_count('jklsdjfoewijrfsdkjfioweujrijsdflsufoiaje;a')) # 7
