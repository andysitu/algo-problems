"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""

"""
& can calculate the carry and ^ can calculate the normal addition

Thus, you can save the carried values and move it forward << 1 for a
normal calculation. After the first ^, the subsequent calculations
are from the carries so you continue until the carries are all
accounted for

Runtime: O(n) - maybe number of binary digits? : space: O(1)
"""

def getSum(self, a: int, b: int) -> int:
    while b > 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a