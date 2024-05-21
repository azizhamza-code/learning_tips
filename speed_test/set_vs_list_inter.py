# this is for testing the speed of set and list for intersection operation for large data

import time
import random

# generate two lists of random numbers
list1 = [random.randint(0, 1000) for i in range(1000)]
list2 = [random.randint(0, 1000) for i in range(1000)]

# convert lists to sets
set1 = set(list1)
set2 = set(list2)

# measure the time taken for intersection
start_time = time.time()
intersection = set1 & set2
end_time = time.time()

print('set intersection took', end_time - start_time)

# measure the time taken for intersection
start_time = time.time()
intersection = [value for value in list1 if value in list2]
end_time = time.time()

print('list intersection took', end_time - start_time)