from datetime import datetime

num_times = 900000
num_integers = 100

# test time for clearing a list
now = datetime.now()

lista = []
for times in range(num_times):
    for i in range(num_integers):
        lista.append(i)

    lista.clear()

later = datetime.now()

print(later - now)


# test time for creating a new one and pointing var to that
now = datetime.now()

lista = None
for times in range(num_times):
    new_list = []
    for i in range(num_integers):
        new_list.append(i)

    lista = new_list

later = datetime.now()

print(later - now)