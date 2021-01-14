from typing import List

class Solution:
    def travel(self, loc, word_string):
        for c in word_string:
            loc = loc[c]
        return loc['@']
    def compare(self, w, l, i, answers, rev):
        while w:
            # print("w", w)
            if '@' in l and w == w[::-1]:
                if rev:
                    answers.append([l['@'], i])
                else:
                    answers.append([i, l['@']])
            c = w.pop()
            # print(c, l)

            if c in l:
                l = l[c]
            else:
                w.append(c)
                break
        # w is empty
        if not w:
            if '@' in l:
                if rev:
                    answers.append([l['@'], i])
                else:
                    answers.append([i, l['@']])
            if 'R' in l:
                for remaining in l['R']:
                    if remaining == remaining[::-1]:
                        if rev:
                            answers.append([self.travel(l, remaining), i])
                        else:
                            answers.append([i, self.travel(l, remaining)])

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        charmap = {}
        rev_charmap = {}
        answers = []

        for i in range(len(words)):
            self.compare(list(words[i]), charmap, i, answers, True)

            self.compare(list(words[i][::-1]), rev_charmap, i, answers, False)

            l = charmap
            w = words[i]
            wlen = len(w)
            # case : ""
            if wlen == 0:
                for j in range(len(words)):
                    if i == j:
                        continue
                    if words[j] == words[j][::-1]:
                        answers.append([i,j])
                        answers.append([j,i])
                continue

            for j in range(len(w)):
                c = w[j]
                if c not in l:
                    l[c] = {'R': []}
                if j != wlen-1:
                    l[c]['R'].append(w[j+1:])
                l = l[c]
            l['@'] = i

            l = rev_charmap
            w = words[i][::-1]
            for j in range(len(w)):
                c = w[j]
                if c not in l:
                    l[c] = {'R': []}
                if j != wlen-1:
                    l[c]['R'].append(w[j+1:])
                l = l[c]
            l['@'] = i
        # print(charmap)
        # print(rev_charmap)
        return answers

s = Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]),'|', [[0,1],[1,0],[3,2],[2,4]]) 
print(s.palindromePairs(["bat","tab","cat"]),'|', [[0,1],[1,0]])
print(s.palindromePairs(["a", ""]),'|', [[0,1],[1,0]])
print(s.palindromePairs(["abcd","dcba","lls","s","sssll", "aa", "b", "a", "", "sll"]),'\n', [[0,1],[1,0],[3,2],[2,9],[3,8],[8,3],[2,4],[5,8],[5,7],[7,5],[8,5],[6,8],[8,6],[7,8],[8,7],[9,3],[9,2]])