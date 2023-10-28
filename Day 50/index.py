# Method of file io

# with statement is used when we automatically close the file.
# with open("myfile.txt", "r") as f:
#     # print(f.readline())
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)


# writeline() method
f = open("myfile2.txt", "w")
lines = ["Hello\n", "world\n", "jaymin\n", "darji\n"]
f.writelines(lines)
f.close()
