def prime_sums(num_limit):
    nums = [False, False]
    sum = 0
    for n in range(2, num_limit+1):
        nums.append(True)
    for n in range(2, num_limit+1):
        if not nums[n]:
            continue
        sum += n
        for factor in range(2, num_limit):
            prod = factor * n
            if prod > num_limit:
                break
            nums[prod] = False
    return sum


print(prime_sums(2000000))
