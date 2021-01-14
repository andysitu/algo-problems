class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set()
        for c in "aeiouAEIOU":
            vowels.add(c)
        vlist = []
        for c in s:
            if c in vowels:
                vlist.append(c)
        slist = list(s)
        for i in range(len(slist)):
            if slist[i] in vowels:
                slist[i] = vlist.pop()
        return "".join(slist)