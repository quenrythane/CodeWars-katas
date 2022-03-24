from timeit import timeit as t

def sum_words(words):
    return ''.join(words)

print(t(str(sum_words())))