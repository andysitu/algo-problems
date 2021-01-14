class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <=3:
            return True
        nlist = [0] * (n+1)
        nlist[0] = 1
        nlist[1] = 1
        nlist[2] = 1
        nlist[3] = 1
        
        for i in range(4, n+1):
            if nlist[i-1] == -1 or nlist[i-2] == -1 or nlist[i-3] == -1:
                nlist[i] = 1
            else:
                nlist[i] = -1
        
        return nlist[n]==1