# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.
"""


def dirReduc(arr):
    steps = []  #
    for step in arr:  #
        steps.append(step)
        if "EAST" in steps[-2:] and "WEST" in steps[-2:]:
            steps.pop(-1)
            steps.pop(-1)
        elif "NORTH" in steps[-2:] and "SOUTH" in steps[-2:]:
            steps.pop(-1)
            steps.pop(-1)

    for step in steps:  #
        if "EAST" in steps[-2:] and "WEST" in steps[-2:]:
            steps.pop(-1)
            steps.pop(-1)
        elif "NORTH" in steps[-2:] and "SOUTH" in steps[-2:]:
            steps.pop(-1)
            steps.pop(-1)
    return steps


def dirReduc2(plan):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_plan = []
    [new_plan.pop() if new_plan and new_plan[-1] == opposite[d] else new_plan.append(d) for d in plan]
    return new_plan


def dirReduc3(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


def dirReduc4(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    for i in range(len(arr) - 1):
        if set(arr[i:i + 2]) in opposites:
            del arr[i:i + 2]
            return dirReduc(arr)
    return arr


def dirReduc5(arr):
    opposite={"NORTH":"SOUTH",
              "SOUTH":"NORTH",
              "WEST":"EAST",
              "EAST":"WEST"
    }
    i=0
    while i+1<len(arr):
        opp=opposite.get(arr[i])
        if arr[i+1]==opp:
            arr.pop(i+1)
            arr.pop(i)
            i=0
        else:
            i+=1
    return arr


def dirReduc6(arr):
    opposite = {"NORTH": "SOUTH",
                "SOUTH": "NORTH",
                "WEST": "EAST",
                "EAST": "WEST"
                }
    i = 0
    while i+1 < len(arr):
        opp = opposite.get(arr[i])
        if arr[i+1] == opp:
            arr.pop(i+1)
            arr.pop(i)
            if i>0:
                i -= 1
        else:
            i += 1
    return arr



import timeit

arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print("dirReduc", timeit.timeit(str(dirReduc(arr)), number=10000))
print("dirReduc2", timeit.timeit(str(dirReduc2(arr)), number=10000))
print("dirReduc3", timeit.timeit(str(dirReduc3(arr)), number=10000))
print("dirReduc4", timeit.timeit(str(dirReduc4(arr)), number=10000))
print("dirReduc5", timeit.timeit(str(dirReduc5(arr)), number=10000))
print("dirReduc6", timeit.timeit(str(dirReduc6(arr)), number=10000))
print("\n")

arr = ['EAST', 'NORTH', 'SOUTH', 'WEST', 'WEST', 'WEST', 'WEST', 'SOUTH', 'NORTH', 'SOUTH', 'WEST', 'WEST', 'EAST', 'SOUTH', 'WEST', 'WEST', 'NORTH', 'SOUTH', 'SOUTH', 'WEST', 'WEST', 'NORTH', 'NORTH', 'WEST']
print("dirReduc", timeit.timeit(str(dirReduc(arr)), number=10000))
print("dirReduc2", timeit.timeit(str(dirReduc2(arr)), number=10000))
print("dirReduc3", timeit.timeit(str(dirReduc3(arr)), number=10000))
print("dirReduc4", timeit.timeit(str(dirReduc4(arr)), number=10000))
print("dirReduc5", timeit.timeit(str(dirReduc5(arr)), number=10000))
print("dirReduc6", timeit.timeit(str(dirReduc6(arr)), number=10000))
