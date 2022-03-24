# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(strng):
    if not strng or strng[-1].isalpha():
        return f"{strng}{1}"

    else:
        for i, ch in enumerate(strng[::-1]):
            y = i
            if ch.isnumeric():
                continue
            else:
                break
    return strng[:-y] + str(int(strng[-y:])+1).zfill(y)


def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


def increment_string3(s):
    if s and s[-1].isdigit():
        return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + `int(s[-1]) + 1`
    return s + "1"


print(increment_string("009"))
