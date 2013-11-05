"""Solution to an exercise in Think Python.

Author: Julie Barron
"""

def top_part(n):
    print '+' + ' - - - - +' * n

def inside_part(n):
    print '|' + '         |' * n

def box(n):
    top_part(n)
    for j in range(n):
        for i in range(4):
            inside_part(n)
        top_part(n)

box(4)