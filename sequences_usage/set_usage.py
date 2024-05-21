# the basic usage of set in python is remove duplicates from a list

my_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
# remove duplicates
my_set = set(my_list)

print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.add(10)

# set elements must be hashable
# so you can't add lists or other sets to a set

# you can frozenset instead
my_set.add(frozenset([1, 2, 3]))


# samrt use of set is to check for membership
# intersection, difference, union, and subset

# membership
print(1 in my_set)  # True

# intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)  # {4, 5}

# difference
print(set1 - set2)  # {1, 2, 3}

# union
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}