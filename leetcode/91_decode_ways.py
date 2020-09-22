class Solution:
    def numDecodings(self, s: str) -> int:
        slen = len(s)
        if slen == 0 or s[0] == '0':
            return 0

        counts = [1] * (slen + 1)

        for i in range(1, slen):
            # Have to use i+1 to save because need prev and prev-prev values
            n = int(s[i])
            prevn = int(s[i-1])
            v = prevn * 10 + n

            if n == 0 and v > 26 or n ==0 and prevn == 0:
                return 0
            elif n == 0:
                counts[i+1] = counts[i-1]
            elif v > 26 or prevn == 0:
                counts[i+1] = counts[i]
            else:
                counts[i+1] = counts[i] + counts[i-1]
            
        return counts[slen]

                

s = Solution()
print(s.numDecodings("2226"))