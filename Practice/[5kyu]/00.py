"""
for i in range(20):
    x = ("00" + str(i))[-3:]
    open(f'{x}.py', 'w')
"""

ml = [1, 2, 3, 4]
# ml[-1] # = 4

print(ml and 4)

x = {1, 2}
print(type(x))

def xyz(arr):
    arr.pop()
    return arr

xd = {'NORTH', 'SOUTH'}
dx = {'NORTH', 'SOUTH'}

for i in range(10000):
    if not xd == dx:
        print('False')
print("coś")


