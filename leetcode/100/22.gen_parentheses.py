class Solution:
    def generateParenthesis(self, n: int):
        if n <= 0:
            return []
        strdict = {"()": True} # current dict of parentheses generated so far
        num_paren = 2
        nums = {1: {"()": True}}
        while num_paren <= n:
            olddict = strdict
            strdict = {}
            for paren_str in olddict:
                # Add () the normal way
                s = "(" + paren_str + ")"
                if s not in strdict:
                    strdict[s] = True
                s = paren_str + "()"
                if s not in strdict:
                    strdict[s] = True
                s = "()" + paren_str
                if s not in strdict:
                    strdict[s] = True

                # Mix and match the old dicts in num
                for num in range(int(num_paren/2), num_paren-1):
                    remain = num_paren - num
                    num_dict = nums[num]
                    remain_dict = nums[remain]
                    for stra in  num_dict:
                        for strb in remain_dict:
                            s = stra + strb
                            if s not in strdict:
                                strdict[s] = True
                            s = strb + stra
                            if s not in strdict:
                                strdict[s] = True
            # Save dict to nums, which records by n
            nums[num_paren] = strdict
            num_paren += 1

        strlist = []
        for k in strdict.keys():
            strlist.append(k)
        return strlist

s = Solution()
print(s.generateParenthesis(10))
