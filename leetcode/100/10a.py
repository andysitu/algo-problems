class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens = len(s)
        lenp = len(p)
        sI = 0
        pI = 0
        matched = False
        while(True):
            print(sI, pI)
            if pI >= lenp or sI >= lens:
                if pI >= lenp and sI >= lens:
                    return True
                elif sI >= lens:
                    if matched:
                        return True
                    elif pI + 1 < lenp and p[pI + 1] == "*":
                        pI += 2
                        continue
                    return False
                elif pI >= lenp:
                    return False
            sCh = s[sI]
            pCh = p[pI]
            if pI + 1 < lenp and p[pI + 1] == "*" and not matched:
                matched = True
            elif matched:
                if pCh == ".":
                    if pI + 2 < lenp:
                        return False
                    return True
                
                if sCh == pCh:
                    sI += 1
                else:
                    matched = False
                    pI += 2
            elif sCh == pCh or pCh == ".":
                sI += 1
                pI += 1
            else:
                return False
        return True
                    
s = Solution()
print(s.isMatch("bbbba", ".*a*a"))
