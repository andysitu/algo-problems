class Solution:
    def groupAnagrams(self, strs):
        sorted_words = {}
        for word in strs:
            w = ''.join(sorted(word))
            if w not in sorted_words:
                sorted_words[w] = []
            sorted_words[w].append(word)
        answer = []
        for wkey in sorted_words:
            answer.append(sorted_words[wkey])
        return answer
            

s = Solution()
print(s.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))