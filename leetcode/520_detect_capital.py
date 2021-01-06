class Solution:
    def isCapital(self, c):
        if ord(c) <= ord('Z'):
            return True
        return False
    def detectCapitalUse(self, word: str) -> bool:
        wordlen = len(word)
        allCapital = True
        someCapital = False
        firstCapital = self.isCapital(word[0])
        
        for i in range(1, wordlen):
            if (self.isCapital(word[i])):
                someCapital = True
            else:
                allCapital = False
        if (firstCapital and allCapital and someCapital):
            return True
        elif not someCapital:
            return True
        return False