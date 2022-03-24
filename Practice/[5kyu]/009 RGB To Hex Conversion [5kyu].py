# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    result = []
    for i in r, g, b:
        if i not in range(0, 256):
            i = 0 if i < 0 else 255
        result.append(hex(i)[2:].upper().zfill(2))
    return ''.join(result)

def rgb2(r, g, b):
    return ''.join([hex(i)[2:].upper().zfill(2) for i in [i if i in range(0, 256) else 0 if i < 0 else 255 for i in [r, g, b]]])


def rgb3(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))



