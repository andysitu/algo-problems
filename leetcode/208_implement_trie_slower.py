class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = [0 for _ in range(27)]
        self.words = set()
        
    
    def conv_index(self, c):
        return ord(c) - ord('a') + 1
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        loc = self.trie
        for c in word:
            l = self.conv_index(c)
            if loc[l] == 0:
                loc[l] = [0 for _ in range(27)]
            loc = loc[l]
        loc[0] = 1
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
            l = self.conv_index(c)
            if loc[l] == 0:
                return False
            loc = loc[l]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)