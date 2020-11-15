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
        wordList.append(beginWord)
        end_diff_dict = {}

        strlen = len(beginWord)

        for i in range(len(wordList)):
            n = self.find_num_diff(endWord, wordList[i], strlen)
            if n not in end_diff_dict:
                end_diff_dict[n] = []
            end_diff_dict[n].append(i)

        print(wordList)
        print(end_diff_dict)

        start_diff_dict = {}

        for i in range(len(wordList)):
            n = self.find_num_diff(beginWord, wordList[i], strlen)
            if n not in start_diff_dict:
                start_diff_dict[n] = []
            start_diff_dict[n].append(i)

        print(start_diff_dict)

        if 0 not in end_diff_dict:
            return []

        end_success_map = {}
        end_success_map[endWord] = [[end_diff_dict[0][0]]]

        start_success_map = {}
        start_success_map[beginWord] = [[start_diff_dict[0][0]]]

        moved_next_level = False

        while not moved_next_level:
            changed = False # status to see if anything changed
            for index in start_diff_dict[1]

        # num_diff - number of chars differetn from start or end word
        for num_diff in range(1, strlen+1):
            if num_diff - 1 not in end_diff_dict:
                return []
            for index in end_diff_dict[num_diff]:
                search_word = wordList[index]
                for searched_word_index in end_diff_dict[num_diff-1]:
                    w = wordList[searched_word_index]
                    # print(search_word, w)
                    if self.find_num_diff(search_word, w, 1) != -1 and w in end_success_map:
                        if search_word not in end_success_map:
                            end_success_map[search_word] = []
                        for paths in end_success_map[w]:
                            end_success_map[search_word].append([index] + paths)

            # for index in start_diff_dict[num_diff]:
            #     print(index, start_success_map)
            #     search_word = wordList[index]
            #     for searched_word_index in start_diff_dict[num_diff-1]:
            #         w = wordList[searched_word_index]
            #         if self.find_num_diff(search_word, w, 1) != -1 and w in end_success_map:
            #             print(search_word, w, start_success_map)
            #             if search_word not in start_success_map:
            #                 start_success_map[search_word] = []
            #             for paths in start_success_map[w]:
            #                 start_success_map[search_word].append([index] + paths)
        print(end_success_map)
        print(start_success_map)
        # match from beginWord and forward until matches are found

        # search with beginWord for n-1 words to see if match

        # if strlen in end_diff_dict:
        #     search_list = end_diff_dict[strlen - 1] + end_diff_dict[strlen]
        # else:
        #     search_list = end_diff_dict[strlen - 1]

        # next_search = []
        # found = []
        # move_on = False
        # found_status = False
        # for index in search_list:
        #     if self.find_num_diff(wordList[index], beginWord, 1) != -1:
        #         move_on = True
        #         if wordList[index] in succes_map:
        #             found = True
        #             found.append(index)
        #         else:
        #             next_search.append(index)

        # print(next_search)
        # print(found)


s = Solution()
print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","log","cog"]))