sequences = "test_me"

# compare list comprehension vs map and filter speed

import timeit

def listcomp():
    return [x for x in sequences if x in 'aeiou']

def map_filter():
    return list(filter(lambda x: x in 'aeiou', sequences))

print(timeit.timeit(listcomp, number=1000000))
print(timeit.timeit(map_filter, number=1000000))
