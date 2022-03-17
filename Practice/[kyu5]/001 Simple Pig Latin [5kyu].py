# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


# Hello world world  elloHay
def pig_it(text):
    from string import punctuation
    return " ".join([text[1:]+text[0]+"ay" if text not in punctuation else text for text in text.split()])


print(pig_it("O tempora o mores !"))
