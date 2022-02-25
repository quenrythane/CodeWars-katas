# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
"""


def find_uniq(arr):
    n1 = arr[0]
    if n1 not in arr[1:3]:
        return n1
    for n in arr[1:]:
        if n1 != n: # 1 != 0
            return n

z1 = [0, 0, 1]
z2 = [1, 0, 0]
z3 = [2, 2, 3, 2, 2, 2]
print(find_uniq(z1))
print(find_uniq(z2))


# znalezione w odpowiedziach. prostszy ale dłużej się wykonuje
def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


