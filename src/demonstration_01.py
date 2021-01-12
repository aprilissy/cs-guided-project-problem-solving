"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

def last(a, n):
    try:
        n = int(n)
    except ValueError as e:
        print(e)
        return 'invalid number'
    if n <= 0:
        return []
    elif len(a) < n:
        return 'invalid'
    return a[-n:]

print(last([1, 2, 3, 4, 5], 1)) # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3)) # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7)) # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0)) # ➞ []
print(last([1, 2, 3, 4, 5], '4')) # ➞ [2, 3, 4, 5]
print(last([1, 2, 3, 4, 5], 'jlj')) # ➞ "invalid number"
