# https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array: list) -> list:
    non_zero_list = []
    zero_list = []
    for n in array:
        non_zero_list.append(n) if n else zero_list.append(n)
    return non_zero_list + zero_list


def move_zeros2(array: list) -> list:
    l = [i for i in array if i != 0]
    return l + [0 for i in range(len(array)-len(l))]


def move_zeros3(array: list) -> list:
    return sorted(array, key=lambda x: x==0)


def wierd_move_zeros_xd(array):
    return sorted(sorted(array, key=lambda x: x < 2), key=lambda x: x==1)


arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(arr))
print(move_zeros2(arr))
print(move_zeros3(arr))
print()
print(wierd_move_zeros_xd(arr))
