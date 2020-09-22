class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stor = []
        slen = len(s)
        sinter = iter(range(slen))
        
        for i in sinter:
            stor_end_index = len(stor) - 1
            if s[i] == "(" and i+1 < slen and s[i+1] == ")": # if () then add num to stor
                if stor_end_index >= 0 and type(stor[stor_end_index]) == int: 
                    # if prev stor add was int then add two nums together
                    stor[stor_end_index] += 2
                else:
                    # else add num
                    stor.append(2)
                next(sinter)
            elif s[i] == ")" \
                and stor_end_index -1 >= 0 and stor[stor_end_index - 1] == "(" \
                    and type(stor[stor_end_index]) == int:
                # If end of stor will consists of "(", [int], ")", then add it together into [int] +2
                num = stor[stor_end_index]
                stor.pop()
                stor[stor_end_index - 1] = num + 2
                if stor_end_index - 2 >= 0 and type(stor[stor_end_index -2]) == int:
                    # After transformation, if prev stor val before the new int is also an int, then add it together
                   stor.pop()
                   stor[stor_end_index -2] += num + 2
            else:
                stor.append(s[i])
        
        max = 0
        for i in range(len(stor)):
            if type(stor[i]) == int and stor[i] > max:
                max = stor[i]
        return max

s = Solution()
print(s.longestValidParentheses("(()"))