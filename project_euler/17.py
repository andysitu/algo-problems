def number_letter_count(number):
    total_sum = 0
    for n in range(1, number+1):
        total_sum += n_count(n)
    return total_sum

def n_count(n):
    num_count = 0
    if n > 10 and n < 20:
            return number_count(n)
    else:
        num_count = 0
        num_str = str(n)
        nstr_len = len(num_str)
        for i in range(nstr_len):
            digit = nstr_len - i
            num = int(num_str[- digit])
            if digit == 2 and num == 1:
                d = digit_count(2, int (num_str[-2] + num_str[-1]))
                num_count += d
                break
            else:
                d = digit_count(digit, num)
                num_count += d
        if n > 100 and (num_str[-1] != "0" or num_str[-2] != "0"):
##                For 'and'
            num_count += 3
        return num_count

def digit_count(digit, num):
    if num == 0:
        return 0
    if digit == 2 and num > 9 and num < 20:
        return number_count(num)
    num_count = number_count(int(num))
    if digit == 4:
        digit_count = number_count(1000)
    elif digit == 3:
        digit_count = number_count(100)
    elif digit == 2:
        num_count = 0
        digit_count = number_count(int( str(num) + "0"))
    else:
        digit_count = 0
##    print(num, digit, num_count, digit_count)
    return num_count + digit_count

def number_count(num):
    if num == 1 or num == 2 or num == 6 or num == 10:
        return 3
    elif num == 3 or num == 7 or num == 8:
        return 5
    elif num == 4 or num == 5 or num == 9:
        return 4
    elif num == 20 or num == 30 or num == 80 or num == 90:
        return 6
    elif num == 40 or num == 50 or num == 60:
        return 5
    elif num == 70:
        return 7
    elif num == 100:
##        return len("hundred")
        return 7
    elif num == 11 or num == 12:
        return 6
    elif num == 13 or num == 14 or num == 18 or num == 19:
        return 8
    elif num == 15 or num == 16:
        return 7
    elif num == 17:
        return 9
    elif num == 1000:
        return 8
    return 0

print(len("onehundredandfifteen"), n_count(115))
print(len("threehundredandfortytwo"), n_count(342))
print(len("onehundredandten"), n_count(110))
print(len("onehundred"), n_count(100))
print(len("ninetynine"), n_count(99))
print(len("ninehundredandninetynine"), n_count(999))
print(len("sixtysix"), n_count(66))
print(len("onehundredandfive"), n_count(105))
print(len("sixhundredandthirtythree"), n_count(633))
print(len("sevenhundredandten"), n_count(710))
print(len("fourhundredandeighteen"), n_count(418))
print(len("nineteen"), n_count(19))

print(number_letter_count(5))
print(number_letter_count(1000))
