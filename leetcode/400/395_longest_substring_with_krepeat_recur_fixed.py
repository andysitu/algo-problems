class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.maxlen = 1 if k == 1 else 0
        
        def check(s, start, end):
            if start > end:
                return
            if end - start + 1 < k:
                return
            counter = [0] * 26
            for i in range(start, end+1):
                counter[ord(s[i]) - ord('a')] += 1
            
            begin = start
            good = True
            for i in range(start, end+1):
                if counter[ord(s[i]) - ord('a')] < k:
                    if i-1 > begin:
                        check(s, begin, i-1)
                    begin = i+1
                    good = False
            if good:
                self.maxlen = max(self.maxlen, end - begin + 1)
            else:
                check(s, begin, end)
        check(s, 0, len(s)-1)
        return self.maxlen