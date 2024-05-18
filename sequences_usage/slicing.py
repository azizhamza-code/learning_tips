# it's easy to see the lenth of the slice : just subtract the start from the end

# its easy to split a string into two parts at a specific index
# just slice the string at that index
s = 'Python'
print(s[:3], s[3:])


# slice s[a:b:c] can be used to specify a stride or step c, which will return every c-th element

# slice s[::-1] can be used to reverse a string
# seq[start:stop:step], Python calls seq.__getitem__(slice(start, stop, step))


# so you can use slice objects to store slices and pass them around

# exemple
# create a slice object
l = [1, 2, 3, 4, 5]

# pair numbers
pair = slice(1, 5, 2)

# pass the slice object to the __getitem__() method of the list

print(l[pair])

l = [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [100, 90]
print(l)