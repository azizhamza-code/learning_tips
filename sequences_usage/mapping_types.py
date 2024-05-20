# all mapping types in python use dict in the background
# so they all share the fact that keys must be hashable

# tip
# my_dict.setdefault(key, []).append(new_value)

# is equivalent to

# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(new_value)

# but the first one is more efficient
# because it only does one lookup in the dictionary
# while the second one does at least two lookups, three if the key is not present

# defaultdict

from collections import defaultdict

# defaultdict is a subclass of dict that returns a default value when a key is not found

# the default value is specified when the defaultdict is created and is called the default_factory

default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['a'])  # 1
print(default_dict['b'])  # 2
print(default_dict['c'])  # 0



