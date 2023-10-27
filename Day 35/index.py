# else with loops

# else with for loop
for i in range(10):
    print(i)
    if i == 4:
        break
else:
    print("sorry i nor found")


print("--------------------------------")

# else with while loop
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("sorry i not found")
