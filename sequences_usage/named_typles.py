# named tuple is consodered as memory efficient 
# because it does not create a new class for each object "__dict__" " is not created for each object 

from collections import namedtuple

# create a named tuple

Point = namedtuple('Point', 'x y')
# is equivalent to namedtuple('Point', ['x', 'y'])
# create an object of Point

p1 = Point(10, 20)
print(p1.x, p1.y)
# access the fields of the named tuple
print(Point._fields)

origin_cordinate = [0, 0]
# create a named tuple from an iterable using _make() method 
origin = Point._make(origin_cordinate)
print(origin)

# _asdict() method returns the named tuple as an OrderedDict
print(origin._asdict())