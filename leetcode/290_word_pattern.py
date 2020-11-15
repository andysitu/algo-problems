class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}
        wordset = set()
        
        slist = s.split(" ")
        
        if len(slist) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in patterns:
                if slist[i] in wordset:
                    return False
                patterns[pattern[i]] = slist[i]
                wordset.add(slist[i])
            else:
                if patterns[pattern[i]] != slist[i]:
                    return False
        return True