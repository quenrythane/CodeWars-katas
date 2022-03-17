# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)

"""


def solution(number):
    result_list = []
    for num in range(number):
        if num % 5 == 0 or num % 3 == 0:
            result_list.append(num)
    return sum(result_list)

def solution2(number):
    return sum([num for num in range(number) if num % 5 == 0 or num % 3 == 0])


print(solution(6))
print(solution2(6))
