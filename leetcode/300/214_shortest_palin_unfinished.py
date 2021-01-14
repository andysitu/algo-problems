class Solution:
    def shortestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen == 1:
            return s

        max_index = 0
        right = slen-1
        while right > 0 and max_index == 0:
            if right % 2 == 0:
                midpoint = int(right/2)
            else:
                midpoint = int(right/2)+1
            palin = True
            for j in range(0, midpoint+1):
                if s[0+j] != s[right-j]:
                    print("error", s[0+j], s[right-j])
                    # print(0+j, right-j, s[0+j], s[right-j])
                    print('start')
                    found = False

                    for shift in range(right-j-1, j, -1):
                        if s[0+j] == s[shift]:
                            found = shift
                            # print(right-j+1, j)
                            # print("SHIFT", shift, s[j], s[shift])
                            # print(0+j, right-j, s[0+j], s[right-j])
                            break
                    
                    if found != False:
                        print("SHIFT", shift, s[j], s[shift], right-j - shift)
                        print("right", right, j)

                    palin = False
                    break
            if palin:
                max_index = right
                break
            right -= 1
            
        if max_index != 0:
            strlist = []
            for i in range(slen-1, max_index, -1):
                strlist.append(s[i])
            return "".join(strlist) + s
        else:
            strlist = []
            for i in range(slen-1, 0, -1):
                strlist.append(s[i])
            return "".join(strlist) + s