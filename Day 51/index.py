# see, tell and some other function in file io.

with open("file.txt", "r") as f:
    # start reading file from index 10
    f.seek(10)

    # read 5 bytes data
    print(f.tell())
    data = f.read(5)
    print(data)


