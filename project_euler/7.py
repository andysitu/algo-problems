
def find_prime(find_num_prime):
    nums = []

    end_num = 9000000

    num_prime = 0

    for i in range(0, end_num+1):
        nums.append(False)

    for i in range(2, end_num+1):
        if nums[i]:
            continue
        else:
            num_prime += 1

            if num_prime == find_num_prime:
                return i
            for factor in range(1, end_num):
                multiplied_num = i * factor
                if multiplied_num > end_num:
                    break
                nums[multiplied_num] = True

    return False


print(find_prime(10001))
