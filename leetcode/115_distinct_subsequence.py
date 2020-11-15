class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        tmap = {}
        for i in range(len(t)):
            t_char = t[i]
        
            if t_char not in tmap:
                tmap[t_char] = []
            tmap[t_char].append(i)
        # print(tmap)

        smap = {}

        for i in range(len(s)):
            s_char = s[i]
            if s_char in tmap:
                if s_char not in smap:
                    smap[s_char] = []
                smap[s_char].append(i)

        places = {} # contains indices of the last character looked at
        # print(smap)
        
        # look through t char by char
        for tindex in range(len(t)-1, -1, -1):
            t_char = t[tindex]

            if t_char not in smap:
                return 0
            else:
                if tindex != len(t) - 1:
                    new_places = {}
                    s_list = smap[t_char]

                    new_s_list = []

                    # look at the indices in s with char t via smap
                    for s_index in s_list:
                        used = False
                        # check if that index against all the indices recorded with the prev t char
                        for index in places:
                            if s_index < index:
                                if s_index not in new_places:
                                    new_places[s_index] = 0
                                new_places[s_index] += places[index]
                                used = True
                        if used:
                            new_s_list.append(s_index)
                    if len(new_places) == 0:
                        return 0
                    smap[t_char] = new_s_list
                    places = new_places
                    # print(places)
                else:
                    s_list = smap[t_char]

                    for s_index in s_list:
                        places[s_index] = 1
        totalcombos = 0
        for num in places:
            totalcombos += places[num]
        return totalcombos

s = Solution()
print(s.numDistinct("rabbbit", "rabbit"))
# 700531452
print(s.numDistinct("adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc", "bcddceeeebecbc"))