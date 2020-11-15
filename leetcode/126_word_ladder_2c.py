from typing import List
import queue

class Solution:
    routes = None
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

    def search(self, diff_map, travel_map, cur_index, cur_level):
        word = self.wordList[cur_index]
        if cur_index in self.routes:
            return self.routes[cur_index]
        else:
            self.routes[cur_index] = []

        # try to match with a word closer matching the end word
        # down a level
        for level_addition in range(-1, 2):
            if level_addition == -1 and cur_level == 0:
                continue
            if level_addition == 1 and cur_level == len(word) - 1:
                continue

            index_table = diff_map[cur_level + level_addition]
            for i in index_table:
                if str(cur_index) + "_" + str(i) in travel_map:
                    continue
                else:
                    travel_map[str(cur_index) + "_" + str(i)] = True
                    if self.find_num_diff(word[cur_index], word[i], 1) != -1:
                        self.search(diff_map, travel_map, i, cur_level + level_addition)
                        next_route = self.routes[i]
                        if len(next_route) != 0:
                            for r in next_route:
                                self.routes[word].append([i] + r)
                        
        
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.routes = {}
        self.travel_map = {}
        self.wordList = wordList

        end_diff_dict = {}

        strlen = len(beginWord)

        num_char_diff = self.find_num_diff(beginWord, endWord, strlen)

        for i in range(len(wordList)):
            n = self.find_num_diff(endWord, wordList[i], strlen)
            if n not in end_diff_dict:
                end_diff_dict[n] = []
            end_diff_dict[n].append(i)
        print(end_diff_dict)


s = Solution()
print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","log","cog"]))