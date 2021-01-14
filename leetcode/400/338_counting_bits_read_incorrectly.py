# This tallies bits in their significant digits

class Solution:
    def countBits(self, num: int) -> List[int]:
        skip = 0
        prev_bit = 0
        bit = 1
        arr = []
        numzeroes = 0
        for i in range(32):
            c = 0
            skip += prev_bit
            n = num - skip
            r = n % (bit*2)
            if r >= bit:
                c += bit
            else:
                c += r
            
            c += (n // (bit * 2)) * bit
            if c == 0:
                if numzeroes == 1:
                    break
                numzeroes += 1
            print(bit, c)
            arr.append(c)
            
            prev_bit = bit
            bit *= 2
        return arr[::-1]