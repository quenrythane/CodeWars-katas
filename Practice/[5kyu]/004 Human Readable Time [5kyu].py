# https://www.codewars.com/kata/52685f7382004e774f0001f7
"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    import time
    x = time.gmtime(seconds)
    return str(f"{('0'+str((x.tm_mday - 1) * 24 + x.tm_hour))[-2:]}:{('0'+str(x.tm_min))[-2:]}:{('0'+str(x.tm_sec))[-2:]}")


def make_readable2(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

print(make_readable(120))
print(make_readable(359999))


