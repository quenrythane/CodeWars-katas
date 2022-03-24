

strng = "asb78adb6ad87ba87sba87"
for i, ch in enumerate(strng[::-1]):
    if ch.isnumeric():
        continue
    else:
        y = i
        break
x = strng[-y:]
print(x)