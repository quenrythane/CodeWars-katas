#https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/python
"""
Hey You !
Sort these integers for me ...

By name ...

Do it now !

Input
Range is 0-999

There may be duplicates

The array may be empty

Example
Input: 1, 2, 3, 4
Equivalent names: "one", "two", "three", "four"
Sorted by name: "four", "one", "three", "two"
Output: 4, 1, 3, 2
Notes
Don't pack words together:
e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"
FUNDAMENTALSSORTINGALGORITHMS
"""

# solution 1
def int_to_word(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    assert(0 <= num)
    if (num < 20):
        return d[num]
    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]
    if (num < 1000):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_word(num % 100)

def sort_by_name(arr):
    return sorted(arr, key=int_to_word)


# solution 2
S = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
     "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENTH = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convertToString(n):
    if not n: return "zero"
    c,t,u = map(lambda v: (n%(v*10))//v, (100,10,1))
    return " ".join(s for s in ["{} hundred".format(S[c]) * bool(c), TENTH[t], S[u+10*(t==1)]] if s)

def sort_by_name2(arr): return sorted(arr, key=convertToString)


# solution 3
def sort_by_name3(arr):
    return sorted(arr, key=convert)

def convert(a):
    if not a: return "zero"
    d = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    r = []
    if a // 100: r.append("{} hundred".format(d[a // 100]))
    if a % 100:
        if a % 100 <= 20: r.append(d[a % 100])
        else:
            b = d[a % 100 // 10 * 10]
            if a % 10: b += " {}".format(d[a % 10])
            r.append(b)
    return " ".join(r)



# solution 4
words = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def num2word(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    else:
        return num2word(n // 100) + " hundred" + (' ' + num2word(n % 100) if n % 100 > 0 else '')

def sort_by_name4(arr):
    return sorted(arr, key=num2word)


# solution 5
S = " one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")
TENTH = "  twenty thirty forty fifty sixty seventy eighty ninety".split(" ")        # Empty strings wanted at the beginning, when splitting!

def convertToString5(n):
    if not n: return "zero"
    c,t,u = map(int, f'{n:0>3}')
    return " ".join(s for s in [f'{S[c]} hundred' * bool(c), TENTH[t], S[u+10*(t==1)]] if s)

def sort_by_name5(arr): return sorted(arr, key=convertToString)



ones_and_tens = ' one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')
ones_and_tens += [f'{ten} {ones_and_tens[one]}' for ten in 'twenty thirty forty fifty sixty seventy eighty ninety'.split() for one in range(10)]
hundreds = [x + ' hundred ' if x else '' for x in ones_and_tens[:10]]

def sort_by_name5(arr):
    return sorted(arr, key=lambda x: hundreds[x//100] + ones_and_tens[x%100] if x else 'zero')

