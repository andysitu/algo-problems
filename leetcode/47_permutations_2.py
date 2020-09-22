class Solution:
    def permuteUnique(self, nums):
        numslen = len(nums)

        a = ['0'] * numslen

        numstable = {1: {}}

        for i in range(numslen):
            a[i] = '1'
            s = ','.join(a)
            a[i] = '0'
            numstable[1][s] = [str(nums[i])]
        
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
                            numstable[i][s] = set()
                        num = nums[j]
                        for prevtable in prevtables[numstr]:
                            numstable[i][s].add(prevtable + ',' + str(num))
                            # numstable[i][s].append([num,] + prevtable)
                        
        r = ['1'] * numslen
        s = ','.join(r)
        numlist = []
        for num_str in numstable[numslen][s]:
            numlist.append([int(x) for x in num_str.split(',')])
        return numlist

s = Solution()
print(s.permuteUnique([1,1,2]))