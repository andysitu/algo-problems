from typing import List

class Solution:
    def checkValid(self, s, index, curWord, leftPan, RightPan, leftRemoved, rightRemoved):
        if leftRemoved > self.maxLeft or rightRemoved > self.maxRight:
            return
        # print(s, index, curWord, leftPan, RightPan, removed)
        if index == len(s):
            if leftPan == RightPan:
                self.answers.add("".join(curWord))
        else:
            if s[index] != '(' and s[index] != ')':
                curWord.append(s[index])
                self.checkValid(s,index+1,curWord,leftPan,RightPan,leftRemoved, rightRemoved)
                curWord.pop()
            else:
                if s[index] == '(':
                    self.checkValid(s,index+1,curWord,leftPan,RightPan,leftRemoved+1, rightRemoved)
                elif s[index] == ')':
                    self.checkValid(s,index+1,curWord,leftPan,RightPan,leftRemoved, rightRemoved+1)
                
                if s[index] ==  '(':
                    curWord.append('(')
                    self.checkValid(s,index+1,curWord,leftPan+1,RightPan,leftRemoved,rightRemoved)
                    curWord.pop()
                elif leftPan > RightPan:
                    curWord.append(')')
                    self.checkValid(s,index+1,curWord,leftPan,RightPan+1,leftRemoved,rightRemoved)
                    curWord.pop()
    
    def calc_paren(self, s):
        left, right = 0,0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                
                if left > 0:
                    left -= 1
        return left, right
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.maxLeft, self.maxRight =self.calc_paren(s)
        self.minRemoved = len(s)
        self.answers = set()
        self.checkValid(s, 0, [], 0, 0, 0, 0)
        return self.answers

s = Solution()
print(s.removeInvalidParentheses("()())()"))