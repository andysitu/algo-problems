class Solution:
    def longestCommonPrefix(self, strs) -> str:
        l = len(strs)
        if l == 0:
            return ""
        elif l == 1:
            return strs[0]
        
        lengths = []
        for i in range(l):
            lengths.append(len(strs[i]))
        
        lengths.sort()
        shortestl = lengths[0]
        s = ""
        for i in range(shortestl):
            a = strs[0][i]
            for j in range(1,l):
                if strs[j][i] != a:
                    return s
            s += a
        return s


s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["a"]))