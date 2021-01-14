from typing import List

class Solution:
    def operate(self, num, start, end, target, pathlist):
        if start > end:
            # print(pathlist)
            new_path = []
            i, j = 0, 0
            pathlen = len(pathlist)
            while i < pathlen:
                p = pathlist[i]
                if p ==  '*':
                    new_path[j-1] = new_path[j-1] * int(pathlist[i+1]) 
                    i += 2
                elif p == '+' or p == '-':
                    new_path.append(p)
                    i += 1
                    j += 1
                else:
                    new_path.append(int(p))
                    i += 1
                    j += 1
            # print(pathlist, new_path)
            n = new_path[0]
            for i in range(1, len(new_path), 2):
                if new_path[i] == '+':
                    n += new_path[i+1]
                else:
                    n -= new_path[i+1]
            if n == target:
                self.answers.append("".join(pathlist))

            return
        
        if num[start] == '0':
            if start == 0:
                self.operate(num, start+1, end, target, pathlist + ['0'])
            else:
                self.operate(num, start+1, end, target, pathlist + ['+', '0'])
                self.operate(num, start+1, end, target, pathlist + ['-', '0'])
                self.operate(num, start+1, end, target, pathlist + ['*', '0'])
        else:
            for i in range(start, end+1):
                n = num[start:i+1]
                if start == 0:
                    self.operate(num, i+1, end, target, pathlist + [n])
                else:
                    self.operate(num, i+1, end, target, pathlist + ['+',  n])
                    self.operate(num, i+1, end, target, pathlist + ['-',  n])
                    self.operate(num, i+1, end, target, pathlist + ['*',  n])
            

    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 0:
            return []
        self.answers = []
        self.operate(num, 0,  len(num)-1, target, [])
        return self.answers

s = Solution()
print(s.addOperators("123", 6))