class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.maxlen = 0
        
        def check(s, start, end):
            if start > end:
                return
            counter = [0] * 26
            for i in range(start, end+1):
                counter[ord(s[i]) - ord('a')] += 1
            
            for i in range(start, end+1):
                if counter[ord(s[i]) - ord('a')] < k:
                    check(s, start, i-1)
                    check(s, i+1, end)
                    return
            self.maxlen = max(self.maxlen, end - start + 1)
        check(s, 0, len(s)-1)
        return self.maxlen