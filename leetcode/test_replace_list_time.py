"""
Test whether it is faster to clear a list or to create a new empty one
and then switching the variables to point to the new list and another variable
to the old one

Result: Inconclusive
"""

from datetime import datetime

num_times = 10000
num_integers = 10000


# test time for clearing a list
now = datetime.now()

lista = []
listb = []
for times in range(num_times):
    for i in range(num_integers):
        listb.append(i)
    temp = lista

    lista = listb
    listb = temp

    listb.clear()

later = datetime.now()

print(later - now)




# test time for creating a new one and pointing var to that
now = datetime.now()

lista = None
prev_list = None
for times in range(num_times):
    prev_list = lista
    new_list = []
    for i in range(num_integers):
        new_list.append(i)

    lista = new_list

later = datetime.now()

print(later - now)

