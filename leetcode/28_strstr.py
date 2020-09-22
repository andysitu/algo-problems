class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        nedlen = len(needle)
        if haylen < nedlen:
            return -1 
        if nedlen <= 0:
            return 0
        for i in range(len(haystack)):
            # Start checking with needle

            # Make sure needle won't exceed haystack in checking
            if i + nedlen > haylen:
                return -1
            if haystack[i] == needle[0]:
                check_status = True
                for a in range(len(needle)):
                    if needle[a] != haystack[i + a]:
                        check_status = False
                        break
                if check_status:
                    return i
        return -1