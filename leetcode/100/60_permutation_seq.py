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
    
    def get_permut(self, n, k):
        if n == 1:
            return ['1',]
        else:
            integer_size = math.factorial(n-1)
            if k > integer_size:
                result = self.get_permut(n, k-integer_size)
                num = math.ceil(k/integer_size)
                numstr = str(num)
                prev_n = str(num-1)

                for i in range(n):
                    if result[i] == numstr:
                        result[i] = prev_n
                        break
                result[0] = numstr
                return result
            else:
                result = self.get_permut(n-1, k)
                return ['1',] + [ self.conv_str(x) for x in result ]


    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(self.get_permut(n, k))


s = Solution()
starttime = datetime.datetime.now()
print(s.getPermutation(5, 68))
# for i in range(1, 25):
#     print(i, s.getPermutation(4, i))  
# for i in range(20, 80, 24):
#     print(i, s.getPermutation(5, i))    
# print(s.getPermutation(4, 20))
# print(s.getPermutation(4, 2))
# print(s.getPermutation(4, 4))
# print(s.getPermutation(4, 5))
# print(s.getPermutation(4, 6))
# print(s.getPermutation(4, 7))
print(s.getPermutation(3, 1)=="123")
print(s.getPermutation(1, 1)=="1")
print(s.getPermutation(3, 3)=="213")
print(s.getPermutation(2, 2)=="21")
print(s.getPermutation(4, 9)=="2314")
print(s.getPermutation(9, 353955)=="972561438")
print(s.getPermutation(9, 362880)=="987654321")

print(datetime.datetime.now()-starttime)
