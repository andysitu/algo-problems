def get_power_sum(powerth):
    num_str = "2"

    for i in range(powerth):
        carry_over = 0
        new_str = ""
        for n in num_str[::-1]:
            num = int(n) * 2 + carry_over
            if num >= 10:
                carry_over = int(num / 10)
                num %= 10
            else:
                carry_over = 0
            new_str = str(num) + new_str
        if carry_over > 0:
            new_str = str(carry_over) + new_str
        num_str = new_str
    sum = 0
    for n in num_str:
        sum += int(n)
    return sum
        

print(get_power_sum(1000))
