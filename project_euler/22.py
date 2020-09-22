from names_file import names


names.sort()
n_len = len(names)

def get_value(l):
    if l=="A":
        return 1
    elif l=="B":
        return 2
    elif l=="C":
        return 3
    elif l=="D":
        return 4
    elif l=="E":
        return 5
    elif l=="F":
        return 6
    elif l=="G":
        return 7
    elif l=="H":
        return 8
    elif l=="I":
        return 9
    elif l=="J":
        return 10
    elif l=="K":
        return 11
    elif l=="L":
        return 12
    elif l=="M":
        return 13
    elif l=="N":
        return 14
    elif l=="O":
        return 15
    elif l=="P":
        return 16
    elif l=="Q":
        return 17
    elif l=="R":
        return 18
    elif l=="S":
        return 19
    elif l=="T":
        return 20
    elif l=="U":
        return 21
    elif l=="V":
        return 22
    elif l=="W":
        return 23
    elif l=="X":
        return 24
    elif l=="Y":
        return 25
    elif l=="Z":
        return 26


total_value = 0
for i in range(0, n_len):
    value = 0
    for letter in names[i]:
        value += get_value(letter)
    total_value += value * (i+1)
print(total_value)
