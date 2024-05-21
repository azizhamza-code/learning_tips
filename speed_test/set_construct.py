# using dis module to see the bytecode

from dis import dis

dis('{1}')
dis('set([1])')


fast_set = {1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9}

slow_set = set([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9])


# the difference between the two sets is that the fast_set is created using a set literal

# while the slow_set is created using the set constructor

# the fast_set is faster because the set literal is optimized by the python interpreter by runing a specialized BUILD_SET bytecode

