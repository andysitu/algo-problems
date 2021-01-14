class Solution:
    def addDigits(self, num: int) -> int:
        nlist = list(str(num))
        nlen = len(nlist)
        for i in range(nlen-2,-1,-1):
            s = int(nlist[i] + nlist[i+1])
            while s >= 10:
                sstr = str(s)
                s = int(sstr[0]) + int(sstr[1])
            nlist[i] = str(s)
        return int(nlist[0])