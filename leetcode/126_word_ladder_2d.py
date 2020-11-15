from typing import List
import queue
import sys

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

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        routes = []
        min_route_length = sys.maxsize
        travel_map = {}
        to_end_route_map = {}
        to_start_route_map = {}

        strlen = len(beginWord)

        num_char_diff = self.find_num_diff(endWord, beginWord, strlen)

        end_diff_dict = {}
        for i in range(len(wordList)):
            if wordList[i] == beginWord:
                continue
            n = self.find_num_diff(endWord, wordList[i], strlen)
            if n not in end_diff_dict:
                end_diff_dict[n] = []
            end_diff_dict[n].append(i)
        # print(end_diff_dict)

        # check if there are words for every transition level
        for i in range(num_char_diff - 1, -1, -1):
            if i not in end_diff_dict:
                return []

        start_diff_dict = {}
        end_index = -1

        for i in range(len(wordList)):
            if wordList[i] == endWord:
                end_index = i
            elif wordList[i] == beginWord:
                continue
            n = self.find_num_diff(beginWord, wordList[i], strlen)
            if n not in start_diff_dict:
                start_diff_dict[n] = []
            start_diff_dict[n].append(i)
        # print(start_diff_dict)
        if end_index == -1:
            return []

        q = queue.Queue()
        # Tuple: (current_level, index, travelled_route, to_end direction)
        q.put((num_char_diff, -1, (-1, ) , 1))
        q.put((num_char_diff, end_index, (end_index, ) , 0))

        while not q.empty():
            word_tup = q.get()
            cur_level = word_tup[0]

            if word_tup[1] == -1:
                cur_word = beginWord
            else:
                cur_word = wordList[word_tup[1]]

            to_end = word_tup[3]
            if to_end:
                start, end, incr = -1, 2, 1
            else:
                start, end, incr = 1, -2, -1
            
            for level_addition in range(start, end, incr):
                if level_addition == -1 and cur_level == 0 or \
                    level_addition == 1 and cur_level == strlen:
                    continue
                
                if to_end:
                    if cur_level + level_addition not in end_diff_dict:
                        continue
                    index_table = end_diff_dict[cur_level + level_addition]
                else:
                    if cur_level + level_addition not in start_diff_dict:
                        continue
                    index_table = start_diff_dict[cur_level + level_addition]

                # explore all the next nodes in the index_table for that level
                for index in index_table:
                    if str(word_tup[1]) + "_" + str(index) in travel_map:
                        continue
                    else:
                        travel_map[str(word_tup[1]) + "_" + str(index)] = True

                        # if the word can be changed by 1 char
                        if self.find_num_diff(cur_word, wordList[index], 1) != -1:
                            
                            # if reached the word, only via to end direction
                            if to_end and cur_level + level_addition == 0:
                                len_route = 1 + len(word_tup[2])
                                if len_route < min_route_length:
                                    min_route_length = len_route

                                routes.append( word_tup[2] + (index,) )
                            # if node has already been found in the opposite dir:
                            elif to_end and index in to_start_route_map:
                                # add it to routes if going to end dir
                                for route_tup in to_start_route_map[index]:
                                    len_route = len(route_tup) + len(word_tup[2])
                                    if len_route > min_route_length:
                                        continue
                                    else:
                                        if len_route < min_route_length:
                                            min_route_length = len_route
                                        r = word_tup[2] + route_tup
                                        routes.append(r)
                            elif not to_end and index in to_end_route_map:
                                # stop the to_start dir, since it's reached the midpoint
                                continue
                            else:
                                if to_end:
                                    r = word_tup[2] + (index,)
                                    if index not in to_end_route_map:
                                        to_end_route_map[index] = []
                                    to_end_route_map[index].append(r)
                                else:
                                    r = (index,) + word_tup[2]
                                    if index not in to_start_route_map:
                                        to_start_route_map[index] = []
                                    to_start_route_map[index].append(r)
                                q.put( ( cur_level + level_addition, index, 
                                        r , word_tup[3]) )
        final_routes = []
        for r in routes:
            if len(r) > min_route_length:
                continue
            new_r = []
            for i in range(len(r)):
                if r[i] != -1:
                    new_r.append(wordList[r[i]])
                else:
                    new_r.append(beginWord)
            final_routes.append(new_r)
        print(routes)

        return final_routes

s = Solution()
# print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","log","cog"]))
# print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","cog"]))
# print(s.findLadders("hit", "cog", ["ait", "hot","dot","dog","lot","log"]))
# print(s.findLadders("hit", "cog", ["ait","dot","dog","lot","log","cog"]))
# print(s.findLadders("hit", "cog", []))
# print(s.findLadders("hit", "cog", ["cog", "ait", "abt", "abc", "abz", "tbz", "cbz", "cgz", "cgf", "cgg", "cgp"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(s.findLadders("a", "c", ["a", "b", "c"]))

p = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]

print(s.findLadders("cet", "ism", p))