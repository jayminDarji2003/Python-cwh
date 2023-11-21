# function caching
# The function caching is a technique used to store information about the function returning.

import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n * n


print("Called for 5 = ", fx(5))
print("Called for 5 = ", fx(10))
print("Called for 5 = ", fx(20))

print("--------------------------------")

print("Called for 5 = ", fx(5))
print("Called for 5 = ", fx(10))
print("Called for 5 = ", fx(20))


"""
    Dryrun :- How this program fun.

        - First of all fx function is called for 5. When the function called wait for 2 seconds.
        - Then same task perform for fx(10) and fx(20).
        - When this 3 function is executed the return value stored somewhere and after that in the second part we did this same work but this time it is not wait for 2 seconds it just fetch the value from the cache. Its all process called caching.

"""
