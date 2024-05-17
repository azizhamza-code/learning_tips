# unpacking is a way to assign multiple values to multiple variables in a single statement


# for exemple os.pth.split() returns a tuple of two values

import os
path = 'my_folder/my_file.txt'
# unpacking the tuple returned by os.path.split()
folder, file = os.path.split(path)
# output: folder: my_folder, file: my_file.txt