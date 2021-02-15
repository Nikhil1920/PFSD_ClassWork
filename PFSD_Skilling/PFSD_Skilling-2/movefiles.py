import os
from pip._vendor.distlib.compat import raw_input
user_input = raw_input("Enter the path of your file: ")
assert os.path.exists(
    user_input), "I did not find the file at, "+str(user_input)
f = open(user_input, "rb")
print("Hooray we found your file!")
k = f.read()
fname = raw_input('Enter the path to copy: ')
f1 = open(fname, 'wb')
f1.write(k)
print("file copied")
