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
    print(saw_numbers)  # [1, 1]

    # 11, 12, 14
    # 21, 22, 24
    # 41, 42, 44
    output = []
    for i in list_of_possible[saw_numbers[0]]:  # 1, 2, 4
        for j in list_of_possible[1]:  # 1, 2, 4
            output.append(str(i) + str(j))

    return output


print(get_pins('11'))
