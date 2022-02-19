"""Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed
him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an
electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it. The keypad
has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another
adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally
lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list
in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the
function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the
results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!
"""


def get_pins(observed: str) -> list:
    # ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"])
    s0 = [0, 8]
    s1 = [1, 2, 4]
    s2 = [1, 2, 3, 5]
    s3 = [2, 3, 6]
    s4 = [1, 4, 5, 7]
    s5 = [2, 4, 5, 6, 8]
    s6 = [3, 5, 6, 9]
    s7 = [4, 7, 8]
    s8 = [0, 5, 7, 8, 9]
    s9 = [6, 8, 9]
    list_of_possible = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    saw_numbers = [int(num) for num in observed]

    output = []
    length = len(observed) - 1
    for i0 in list_of_possible[saw_numbers[0]]:
        if length == 0:
            output.append(str(i0))
        else:
            for i1 in list_of_possible[saw_numbers[1]]:
                if length == 1:
                    output.append(str(i0)+str(i1))
                else:
                    for i2 in list_of_possible[saw_numbers[2]]:
                        if length == 2:
                            output.append(str(i0)+str(i1)+str(i2))
                        else:
                            for i3 in list_of_possible[saw_numbers[3]]:
                                if length == 3:
                                    output.append(str(i0) + str(i1) + str(i2)+str(i3))
                                else:
                                    for i4 in list_of_possible[saw_numbers[4]]:  # 1, 2, 4
                                        if length == 4:
                                            output.append(str(i0) + str(i1) + str(i2)+str(i3)+str(i4))
                                        else:
                                            for i5 in list_of_possible[saw_numbers[5]]:  # 1, 2, 4
                                                if length == 5:
                                                    output.append(str(i0) + str(i1) + str(i2)+str(i3)+str(i4)+str(i5))
                                                else:
                                                    for i6 in list_of_possible[saw_numbers[6]]:  # 1, 2, 4
                                                        if length == 6:
                                                            output.append(str(i0) + str(i1) + str(i2)+str(i3)+str(i4)+str(i5)+str(i6))
                                                        else:
                                                            for i7 in list_of_possible[saw_numbers[7]]:  # 1, 2, 4
                                                                if length == 7:
                                                                    output.append(str(i0) + str(i1) + str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7))
    return output


print(get_pins('11'))
print(get_pins('369'))
# ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]


# ALTERNATIVES:
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/solutions/python
"""
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
"""

"""
adjacents = {
  '1': ['2', '4'],
  '2': ['1', '5', '3'],
  '3': ['2', '6'],
  '4': ['1', '5', '7'],
  '5': ['2', '4', '6', '8'],
  '6': ['3', '5', '9'],
  '7': ['4', '8'],
  '8': ['5', '7', '9', '0'],
  '9': ['6', '8'],
  '0': ['8'],
}

def get_pins(observed):
  if len(observed) == 1:
    return adjacents[observed] + [observed]
  return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]
"""

"""
def get_pins(observed):
  map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]
"""

"""
from itertools import product


PIN = {'1': ('1', '2', '4'), 
       '2': ('1', '2', '3', '5'), 
       '3': ('2', '3', '6'), 
       '4': ('1', '4', '5', '7'), 
       '5': ('2', '4', '5', '6', '8'), 
       '6': ('5', '6', '9', '3'), 
       '7': ('4', '7', '8'), 
       '8': ('7', '5', '8', '9', '0'), 
       '9': ('6', '8', '9'), '0': ('0', '8')}


def get_pins(observed):
    return [''.join(a) for a in product(*(PIN[b] for b in observed))]
"""

