class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        value = "1"
        for i in range(n-1):
            cur_char = value[0]
            count = 1
            new_value = ""
            for i in range(1, len(value)):
                if cur_char == value[i]:
                    count += 1
                else:
                    new_value += str(count) + cur_char
                    cur_char = value[i]
                    count = 1
            new_value += str(count) + cur_char
            value = new_value
        return value
    
s = Solution()
print(s.countAndSay(5))