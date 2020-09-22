def find_divisors(num):
    divisors = [1,]
    sqr = int(num ** (1/2))
    if sqr**2 == num:
        divisors.append(sqr)
    for i in range(2,sqr):
        if num % i == 0:
            j = num / i
            divisors.append(i)
            divisors.append(int(j))
    return divisors

divisors_dic ={}

for i in range(2, 10000):
    divisors = find_divisors(i)
    dsum = 0
    for n in divisors:
        dsum += n
    divisors_dic[i] = dsum

nsums = 0

for a in divisors_dic:
    b = divisors_dic[a]
    if a != b and b in divisors_dic and divisors_dic[b] == a:
        nsums+= a
        print(a, b)
print(nsums)
