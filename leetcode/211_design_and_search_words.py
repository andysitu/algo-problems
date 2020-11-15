class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.words = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        loc = self.trie
        for c in word:
            if c not in loc:
                loc[c] = {}
            loc = loc[c]
        loc["*"] = True
        self.words.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word in self.words:
            return True
        else:
            return self.search_loc(self.trie, word, 0, len(word)-1)
        
    def search_loc(self, loc, word, i, end):
        if i > end:
            if "*" in loc:
                return True
            return False
        else:
            if word[i] == '.':
                result = False
                for c in loc:
                    if c != '*' and self.search_loc(loc[c], word, i+1, end):
                        return True
                return False
            else:
                if word[i] in loc and self.search_loc(loc[word[i]], word, i+1, end):
                        return True
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)