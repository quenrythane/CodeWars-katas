# https://www.codewars.com/kata/60a94f1443f8730025d1744b/train/python
"""
grid(4)

a b c d
b c d e
c d e f
d e f g
grid(10)

a b c d e f g h i j
b c d e f g h i j k
c d e f g h i j k l
d e f g h i j k l m
e f g h i j k l m n
f g h i j k l m n o
g h i j k l m n o p
h i j k l m n o p q
i j k l m n o p q r
j k l m n o p q r s
Notes:
After "z" comes "a"
If function receive N < 0 should return:
"""


from string import ascii_lowercase
def grid(N):
    if N < 0:
        return None
    low = ascii_lowercase*10
    result = ""
    for i in range(N):
        result += ' '.join(low[i:N+i]) + '\n'
    return result[:-1]

from string import ascii_lowercase
def grid2(N):
    low = ascii_lowercase*10
    return None if N < 0 else ''.join([' '.join(low[i:N+i]) + '\n' for i in range(N)])[:-1]


print(grid(4), "\n")
print(grid2(1), "\n")
print(grid2(4), "\n")
print(grid(-1), "\n")
