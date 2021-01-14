class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        slen = len(s)
        for i in range(slen//2):
            s[i], s[slen-i-1] = s[slen-i-1], s[i]