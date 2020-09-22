
num = 0

while(True):
    num += 1
    sum_num = 0
    for i in range(1,num):
        sum_num += i

    factors = {}

    for i in range(1, num):
        if sum_num % i == 0:
            factors[i] = True
            factors[int(sum_num / i)] = True
    if len(factors) > 500:
        break

print(sum_num)
