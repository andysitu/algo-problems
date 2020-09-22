class Solution:
    def permute(self, nums):
        numslen = len(nums)

        a = ['0'] * numslen

        numstable = {1: {}}

        for i in range(numslen):
            a[i] = '1'
            s = ','.join(a)
            a[i] = '0'
            numstable[1][s] = [[nums[i]]]
        
        for i in range(2, numslen+1):
            numstable[i] = {}
            prevtables = numstable[i-1]
            for numstr in prevtables:
                indexlist = numstr.split(',')
                indexlistlen = len(indexlist)
                for j in range(indexlistlen):
                    nl_value = indexlist[j]
                    if nl_value == "0":
                        indexlist[j] = '1'
                        s = ','.join(indexlist)
                        indexlist[j] = '0'
                        if s not in numstable[i]:
                            numstable[i][s] = []
                        num = nums[j]
                        for prevtable in prevtables[numstr]:
                            numstable[i][s].append(prevtable + [num,])
                            # numstable[i][s].append([num,] + prevtable)
                        
        r = ['1'] * numslen
        s = ','.join(r)
        return numstable[numslen][s]

s = Solution()
a = []
for i in range(1, 1000000):
    a.append(i)
print(s.permute([1,2,3]))
print(s.permute([1,2,3,4,5,6,7,8,9]))