class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.words = set()
                

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        loc = self.trie
        for c in word:
            if c not in loc:
                loc[c] = {}
            loc = loc[c]
        self.words.add(word)
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        loc = self.trie
        for c in prefix:
            if c not in loc:
                return False
            loc = loc[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)