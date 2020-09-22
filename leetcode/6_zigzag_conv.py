def convert(s, numRows):
    stor = {}
    for i in range(numRows):
        stor[i] = []
    num_spaces = 0
    len_s = len(s)
    i_s = 0
    while(i_s < len_s):
        if (num_spaces == 0):
            for i in range(numRows):
                stor[i].append(s[i_s])
                i_s += 1
                if (i_s >= len_s):
                    break
                num_spaces = 0
            num_spaces = numRows - 2
            if (num_spaces <= 0):
                num_spaces = 0
        else:
            stor[num_spaces].append(s[i_s])
            i_s += 1
            num_spaces -= 1
    word = ""
    for i in range(numRows):
        word += ''.join(stor[i])
    return word

print(convert("AB", 1))