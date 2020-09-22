sums_num = 0

def find_divisors(num):
    divisors = [1,]

    d = {}
    sqr = int(num ** (1/2))
    for i in range(2,sqr+1):
        if num % i == 0:
            j = num / i
            d[i] = 0
            d[int(j)] = 0
    for x in d:
        divisors.append(x) 
    return divisors

abundant_nums = {}

sums_abundant_nums = {x: 0 for x in range(1,28124)}

for n in range(12, 28124):
    divisors = find_divisors(n)
    sum_divisors = sum(divisors)
    if sum_divisors > n:
        abundant_nums[n] = 0

for a in abundant_nums:
    for b in abundant_nums:
        if a + b < 28124:
            sums_abundant_nums[a+b] = 1

for number in sums_abundant_nums:
    if sums_abundant_nums[number] == 0:
        sums_num += number

print(sums_num)
