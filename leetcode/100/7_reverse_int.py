def reverse(self, x: int) -> int:
    if x >= 2 **31 -1 or x <= -2**31:
        return 0
    a = str(x)
    lena = len(a)
    b = ''

    if x < 0:
        neg = -1
        end = 0
    else:
        neg = 1
        end = -1
    for i in range(lena-1, end, -1):
        b += a[i]
    value = int(b)
    if neg*value >= 2 **31 -1 or neg*value <= -2**31:
        return 0
    else:
        return neg * value
print(reverse(-123))