import math

import datetime

class Solution:
    @staticmethod
    def conv_str(s):
        if s == '1':
            return '2'
        elif s == '2':
            return '3'
        elif s == '3':
            return '4'
        elif s == '4':
            return '5'
        elif s == '5':
            return '6'
        elif s == '6':
            return '7'
        elif s == '7':
            return '8'
        elif s == '8':
            return '9'

    def getPermutation(self, n: int, k: int) -> str:
        if k == 1 and n == 1:
            return '1'
        values = [x for x in range(1,n+1)]

        combos = [['1']]
        count = 0
        first_s_change = 0

        for level in range(2, n+1):
            prev_numtimes = math.factorial(level-1)
            numtimes = math.factorial(level)
            prev_combos = combos
            combos = []
            prev_numstr_length = len(prev_combos[0])

            for t in range(numtimes):
                start_n = int(t/prev_numtimes)+1
                index = t % prev_numtimes

                if start_n == 1:
                    num_str = prev_combos[t]
                    new_str = ['1',]
                    for s in num_str:
                        new_str.append(Solution.conv_str(s))
                else:
                    num_str = combos[ (start_n -2) * prev_numtimes + index ]

                    start_nstr = str(start_n)
                    prev_nstr = num_str[0]
                    new_str = list(num_str)
                    new_str[0] = start_nstr

                    nlen = len(num_str)
                    for i in range(1, nlen):
                        s = num_str[i]

                        if s == start_nstr:
                            new_str[i] = prev_nstr
                            break
                if level == n:
                    count += 1
                    if count == k:
                        return ''.join(new_str)
                combos.append(new_str)
        return ''.join(combos[k-1])


s = Solution()
starttime = datetime.datetime.now()
print(s.getPermutation(5, 68))
for i in range(1, 25):
    print(i, s.getPermutation(4, i))  
for i in range(20, 80, 24):
    print(i, s.getPermutation(5, i))    
# print(s.getPermutation(4, 20))
# print(s.getPermutation(4, 2))
# print(s.getPermutation(4, 4))
# print(s.getPermutation(4, 5))
# print(s.getPermutation(4, 6))
# print(s.getPermutation(4, 7))
# print(s.getPermutation(3, 1)=="123")
# print(s.getPermutation(1, 1)=="1")
# print(s.getPermutation(3, 3)=="213")
# print(s.getPermutation(2, 2)=="21")
# print(s.getPermutation(4, 9)=="2314")
# print(s.getPermutation(9, 353955)=="972561438")
# print(s.getPermutation(9, 362880)=="987654321")

print(datetime.datetime.now()-starttime)
