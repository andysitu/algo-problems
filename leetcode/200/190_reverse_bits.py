class Solution:
    def reverseBits(self, n: int) -> int:
        newn = n
        result = 0

        for i in range(32):
            result = result << 1
            result = result | newn&1
            # print("{0:b}".format(result))
            newn = newn >> 1
            
        return result

s = Solution()
s.reverseBits()