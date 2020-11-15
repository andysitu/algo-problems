from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = set()
        repeats = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in dna:
                dna.add(s[i:i+10])
            else:
                if s[i:i+10] not in repeats:
                    repeats.add(s[i:i+10])
        return repeats

s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
