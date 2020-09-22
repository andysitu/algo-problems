def factorial(n):
    prod = "1"
    for i in range(2, n+1):
        new_prod = ""
        prod_rev = prod[::-1]
        carry_over = 0
        for n in prod_rev:
            num = int(n)
            p = num * i + carry_over
            if p >= 10:
                carry_over = int(p / 10)
                p %= 10
            else:
                carry_over = 0
            new_prod = str(p) + new_prod
        if carry_over != 0:
            new_prod = str(carry_over) + new_prod
        prod = new_prod
    return prod

def sum_factorial(n):
    num_str = factorial(n)
    sums = 0

    for i in num_str:
        sums += int(i)
    return sums

print(sum_factorial(10))
