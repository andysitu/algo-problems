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
            
            begin = 0
            for i in range(start, end+1):
                if counter[ord(s[i]) - ord('a')] < k:
                    if i-1 > begin:
                        check(s, begin, i-1)
                    begin = i+1
            if end > begin and end - begin + 1 >= k:
                print(begin, end)
                self.maxlen = max(self.maxlen, end - begin + 1)
        check(s, 0, len(s)-1)
        return self.maxlen

# count resets after the pivot point