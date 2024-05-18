my_list = [[]] * 3
my_list[0].append(1)
print(my_list)


# with sequences

# when using += operation if the __iadd__() method is not implemented, the __add__() method is called


# the same is true for the *=,  __imul__() and __mul__() methods


l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))
