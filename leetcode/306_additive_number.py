class Solution:
    def adder(self, num, start, end, num1, num2):
        if start > end:
            return True
        s = num1+num2
        if s in self.numdict and start in self.numdict[s]:
            return self.adder(num, self.numdict[s][start]+1, end,  num2, s)
        return False

    def isAdditiveNumber(self, num: str) -> bool:
        nlen = len(num)
        if nlen <= 2:
            return False
        self.numdict = numdict = {}
        self.numarr = numarr = []
        
        for i in range(nlen):
            numarr.append([0] * nlen)
            if num[i] == '0':
                if 0 not in numdict:
                    numdict[0] = {}
                numdict[0][i]=i
                continue
            for j in range(i+1, nlen+1):
                n = int(num[i:j])
                if n not in numdict:
                    numdict[n] = {}
                
                numdict[n][i]=j-1
                numarr[i][j-1]=n
        # print(numarr)
        # print(numdict)
        endj = 2 if num[0] == '0' else nlen-1

        for j in range(1,endj):
            endk = j+1 if num[j] == '0' else nlen -1
            for k in range(j, endk):
                # print(i,j,k)
                if self.adder(num, k+1, nlen-1, numarr[0][j-1], numarr[j][k]):
                    return True
        return False

s = Solution()
# print(s.isAdditiveNumber("113422358"), False)
# print(s.isAdditiveNumber("112358"), True)
# print(s.isAdditiveNumber("199100199"), True)
print(s.isAdditiveNumber("123"), True)
print(s.isAdditiveNumber("0111122"), True)
print(s.isAdditiveNumber("00111122"), False)
print(s.isAdditiveNumber("01101122"), False)