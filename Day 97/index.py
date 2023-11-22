'''
    Multithreading in python.
        -> When we want to get data from different different servers at the same time then we need to use multithreading.

        Let's take example :-
            Question :- we have five server.all the server have 10gb 10gb of data.we want to get all the data from all the servers.

            answer;

            first way:- download from one server then download from another server.

            second way :- download all the data from all the servers at the same time.
'''

import threading
import time

# Indicates some task being done
def get_data(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)

# normal code 
# get_data(2)
# get_data(4)
# get_data(2)

# same code using Threads
t1 = threading.Thread(target=get_data, args=[2])
t2 = threading.Thread(target=get_data, args=[4])
t3 = threading.Thread(target=get_data, args=[2])

t1.start()
t2.start()
t3.start()