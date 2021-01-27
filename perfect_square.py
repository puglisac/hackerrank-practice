"""
Write a Python program to check if a number is a perfect square. 
>>> is_perfect_square(25)
True
>>> is_perfect_square(43)
False
"""

def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True


