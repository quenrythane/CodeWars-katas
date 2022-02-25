# https://www.codewars.com/kata/57eae65a4321032ce000002d
"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the
resulting string.

Note: input will never be an empty string
"""


def fake_bin(x):
    return "".join('0' if int(n) < 5 else '1' for n in x)

