# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""

def first_non_repeating_letter(string):
    counter = {}
    for ch in string.lower():
        if ch not in counter:
            counter[ch] = 1
        else:
            counter[ch] += 1
    for k, v in counter.items():
        if v == 1:
            return string[string.lower().find(k)]
    return ""


def first_non_repeating_letter1(string):
    return ''.join([i for i in string if string.lower().count(i.lower()) == 1][:1])


def first_non_repeating_letter2(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]


def first_non_repeating_letter3(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''


def first_non_repeating_letter4(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''


def first_non_repeating_letter5(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''


def first_non_repeating_letter7(string):
    return next((x for x in string if string.lower().count(x.lower()) == 1), '')

