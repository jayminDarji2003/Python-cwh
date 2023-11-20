# Time module in python

import time

print(time.time())  # return current time in seconds

print("Wait for 5 seconds to complete the task...")
#time.sleep(5) # wait for 5 seconds
print("Done!")

t = time.localtime()
print(t)
print(time.strftime("%H hour",t))  # return hour
print(time.strftime("%M minute",t))  # return minute
print(time.strftime("%S seconds",t))  # return second

print(time.strftime("%d date",t))  # return date
print(time.strftime("%m month",t))  # return month
print(time.strftime("%Y year",t))  # return year