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
    start_list = start.split('.')
    end_list = end.split('.')
    return start_list, end_list


print(ips_between("10.0.0.0", "10.0.0.50"), "should 50")
print(ips_between("20.0.0.10", "20.0.1.0"), "should 246")
