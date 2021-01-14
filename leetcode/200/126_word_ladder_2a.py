from typing import List
import queue

class Solution:
    def print_dict(self, dict):
        for k in dict:
            print(k, dict[k])
    def find_num_diff(self, s1, s2, max_diff):
        num_diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diff += 1
                if num_diff > max_diff:
                    return -1
        return num_diff

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        diff_dict = {}

        strlen = len(beginWord)

        for i in range(len(wordList)):
            n = self.find_num_diff(endWord, wordList[i], strlen)
            if n not in diff_dict:
                diff_dict[n] = []
            diff_dict[n].append(i)

        print(wordList)
        print(diff_dict)

        if 0 not in diff_dict:
            return []

        succes_map = {}
        succes_map[endWord] = [[diff_dict[0][0]]]

        # search from endWord back       
        for num_diff in range(1, strlen+1):
            if num_diff - 1 not in diff_dict:
                return []
            for index in diff_dict[num_diff]:
                search_word = wordList[index]
                for searched_word_index in diff_dict[num_diff-1]:
                    w = wordList[searched_word_index]
                    # print(search_word, w)
                    if self.find_num_diff(search_word, w, 1) != -1 and w in succes_map:
                        if search_word not in succes_map:
                            succes_map[search_word] = []
                        for paths in succes_map[w]:
                            succes_map[search_word].append([index] + paths)
        print(succes_map)
        # match from beginWord and forward until matches are found

        # search with beginWord for n-1 words to see if match

        if strlen in diff_dict:
            search_list = diff_dict[strlen - 1] + diff_dict[strlen]
        else:
            search_list = diff_dict[strlen - 1]

        next_search = []
        found = []
        move_on = False
        found_status = False
        for index in search_list:
            if self.find_num_diff(wordList[index], beginWord, 1) != -1:
                move_on = True
                if wordList[index] in succes_map:
                    found = True
                    found.append(index)
                else:
                    next_search.append(index)

        print(next_search)
        print(found)


s = Solution()
print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","log","cog"]))