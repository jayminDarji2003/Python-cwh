# File IO

# open() method
# Open method is used to open a file.It takes two arguments: 1. filename and 2. mode(r,w,a).


# READING A FILE

# file = open("myfile.txt", "r")

# read the file
# fileTxt = file.read()
# print(fileTxt)

# close the file
# file.close()


# WRITING TO THE FILE
# f = open("myfile2.txt", "w")
# f.write("Hello, world!")
# f.close()

# APPEND THE FILE
# f = open("myfile2.txt", "a")
# f.write("Hello, world!")
# f.close()

f = open("myfile2.txt", "r")
txt = f.read()
# txt = f.readlines()
print(txt)
f.close()
