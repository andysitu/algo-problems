class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if s[i] not in sdict:
                if t[i] in tdict:
                    return False
                sdict[s[i]] = t[i]
                tdict[t[i]] = s[i]
            else:
                if sdict[s[i]] !=  t[i] or tdict[t[i]] != s[i]:
                    return False
        return True