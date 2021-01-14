class Solution:
    def isValid(self, s):
        parenData = [] # stores parantheses

        for c in s: # c for char
            if c == "(" or c == "{" or c == "[":
                parenData.append(c)
            elif c == ")" or c == "}" or c == "]":
                l = len(parenData)
                if l == 0:
                    return False
                c_prev = parenData[l-1] # Get last char added to parenData & compare
                # If it doesn't close correctly
                if (c == ")" and c_prev != "(") or \
                    (c == "}" and c_prev != "{") or \
                    (c == "]" and c_prev != "["):
                    return False
                parenData.pop(l-1)
            else:
                return False
        if len(parenData) == 0:
            return True
        else:
            return  False

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("(])"))
print(s.isValid("()()[]{}"))
print(s.isValid("{}{{{}}}{()}[][][[[[()]]]]"))
print(s.isValid("{}{{{}}}{()}[][f][[[[()]]]]"))
print(s.isValid("{}{{{}}}{()}[][(][[[[()]]]]"))
print(s.isValid("]"))