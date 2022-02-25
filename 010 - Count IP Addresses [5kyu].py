# https://www.codewars.com/kata/526989a41034285187000de4
"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the
first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50
ips_between("10.0.0.0", "10.0.1.0")   ==  256
ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""


def ips_between(start, end):
    start_list = [int(w) for w in start.split('.')]
    end_list = [int(w) for w in end.split('.')]
    result = 0
    for i in range(4):
        result += (end_list[i] - start_list[i]) * 256 ** (3-i)
    return result


print(ips_between("10.0.0.0", "10.0.0.50"),  "should 50")
print(ips_between("20.0.0.10", "20.0.1.0"), "should 246")

# ALTERNATIVES: https://www.codewars.com/kata/526989a41034285187000de4/solutions/python
"""
from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))
"""

"""
def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)
"""