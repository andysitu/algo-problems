class Solution:
    def isPalindrome(self, s: str, i1, i2) -> bool:
        slen = i2-i1+1
        if slen % 2 == 0:
            end = int(slen / 2)
        else:
            end = int(slen / 2) + 1
        # print(self.palindrome_map)
        result = True
        for i in range(end):
            # print(i, slen-i-1)
            if  self.palindrome_map[i1+ i][i1 + slen-i-1] == 1:
                result = True
                break
            elif  self.palindrome_map[i1 + i][i1 + slen-i-1] == 0:
                result = False
                break
            else:
                if s[i1 + i] != s[i1 + slen-i-1]:
                    result = False
                    break
        
        if result:
            numresult = 1
        else:
            numresult = 0
        for index in range(i, -1, -1):
            # print(index, slen-index-1)
            self.palindrome_map[i1+ index][i1+ slen-index-1] = numresult

        return result

    def minCut(self, s: str) -> int:
        slen = len(s)
        self.palindrome_map = []
        for i in range( slen ):
            self.palindrome_map.append([-1] * slen)

        min_arrs = [slen] * slen
        min_arrs[slen - 1] = 1

        for i in range(slen -2, -1, -1):
            min_value = slen
            for index in range(slen-1, i-1, -1):
                # print(i, index, s[i:index+1])
                if self.isPalindrome(s, i, index):
                    if index == slen-1:
                        min_value = 1
                        break
                    else:
                        min_value = min(min_value, 1 + min_arrs[index+1])
            min_arrs[i] = min_value

        # print(self.palindrome_map)
        # print(min_arrs)
        return min_arrs[0] - 1