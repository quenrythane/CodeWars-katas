# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function
 should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input
 string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

# hi())(            =>  false
# ")(()))"          =>  false
# "(())((()())())"  =>  true
# hi(hi)()


def valid_parentheses(string):
    x = 0  # opening
    y = 0  # closing
    for i in string:
        if i == '(':
            x += 1
        elif i == ')':
            y += 1

        if y > x:
            return False
    return x == y


def valid_parentheses2(string):
    cnt = 0
    for char in string:
        if char == '(':
            cnt += 1
        if char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return not cnt


def valid_parentheses3(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string:
        string = string.replace("()", "")
    return not string
