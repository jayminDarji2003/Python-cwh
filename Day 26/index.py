# Exercise 2 : solution

# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current time.
"""
    Good morning -> 0 to 12 
    Good afternoon -> 12 to 16 (4)
    Good evening -> 16 (4) to 24 (12)
"""

import time

# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)

hour = int(time.strftime("%H"))
print(hour)

if hour <= 12:
    print("Good Morning")
elif hour > 12 and hour <= 16:
    print("Good Afternoon")
elif hour > 16 and hour <= 24:
    print("Good Evening")
