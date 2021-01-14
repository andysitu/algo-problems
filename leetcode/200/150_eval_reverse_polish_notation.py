class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


"""
["4444444444", "1000", "5", "/", "3", "/", "/"]
["4","-2","/","2","-3","-","-"]
"""