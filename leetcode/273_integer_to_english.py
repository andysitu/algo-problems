class Solution:
    def one_num(self, n):
        if n == '1':
            return "One"
        elif n == '2':
            return "Two"
        elif n == '3':
            return "Three"
        elif n == '4':
            return "Four"
        elif n == '5':
            return "Five"
        elif n == '6':
            return "Six"
        elif n == '7':
            return "Seven"
        elif n == '8':
            return "Eight"
        elif n == '9':
            return "Nine"
        else:
            return ""
        
    def three_num(self, nums, nlist):
        nlen = len(nums)
        if nlen >= 2 and nums[1] == '1':
            if nums[0] == '0':
                nlist.append("Ten")
            elif nums[0] == '1':
                nlist.append("Eleven")
            elif nums[0] == '2':
                nlist.append("Twelve")
            elif nums[0] == '3':
                nlist.append("Thirteen")
            elif nums[0] == '4':
                nlist.append("Fourteen")
            elif nums[0] == '5':
                nlist.append("Fifteen")
            elif nums[0] == '6':
                nlist.append("Sixteen")
            elif nums[0] == '7':
                nlist.append("Seventeen")
            elif nums[0] == '8':
                nlist.append("Eighteen")
            elif nums[0] == '9':
                nlist.append("Nineteen")
        else:
            if nums[0] != '0':
                nlist.append(self.one_num(nums[0]))
        
        if nlen >= 2:
            if nums[1] == '2':
                nlist.append("Twenty")
            if nums[1] == '3':
                nlist.append("Thirty")
            if nums[1] == '4':
                nlist.append("Forty")   
            if nums[1] == '5':
                nlist.append("Fifty")
            if nums[1] == '6':
                nlist.append("Sixty")
            if nums[1] == '7':
                nlist.append("Seventy")
            if nums[1] == '8':
                nlist.append("Eighty")
            if nums[1] == '9':
                nlist.append("Ninety")
        
        if nlen == 3 and nums[2] != '0':
                nlist.append("Hundred")
                nlist.append(self.one_num(nums[2]))
                
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        nstr = str(num)[::-1]
        nlist = []
        self.three_num(nstr[:3], nlist)

        nlen = len(nstr)

        if nlen > 3:
            nlist.append("Thousand")
            nlistprev = len(nlist)
            self.three_num(nstr[3:6], nlist)
            if len(nlist) == nlistprev:
                nlist.pop()
        if nlen > 6:
            nlist.append("Million")
            nlistprev = len(nlist)
            self.three_num(nstr[6:9], nlist)
            if len(nlist) == nlistprev:
                nlist.pop()
        if nlen >= 10:
            nlist.append("Billion")
            self.three_num(nstr[9:10], nlist)
        return " ".join(nlist[::-1])

            
        

s = Solution()
s.numberToWords("2423231105")