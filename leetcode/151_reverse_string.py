class Solution:
    def reverseWords(self, s: str) -> str:
        start_index = None
        new_s = ""
        for i in range(len(s)):
            if start_index == None:
                if s[i] != ' ':
                    start_index = i
            else:
                if s[i] == ' ' and start_index != None:
                    new_s = s[start_index: i] + ' ' + new_s
                    start_index = None
        if s[len(s) - 1] != ' ':
            new_s = s[start_index: len(s)] + ' ' + new_s
        if new_s[len(new_s) - 1] == ' ':
            return new_s[:len(new_s)-1]
        return new_s