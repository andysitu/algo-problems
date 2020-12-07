from typing import List

class Solution:
    def travel(self, loc, word_string):
        for c in word_string:
            loc = loc[c]
        return loc['@']
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        charmap = {}
        rev_charmap = {}
        answers = []

        for i in range(len(words)):
            w = words[i]
            l = charmap 
            # 'popping' chars so going in rev
            while w:
                if '@' in l and w == w[::-1]:
                    answers.append([l['@'], i])
                c = w[-1]

                if c in l:
                    l = l[c]
                else:
                    break
                w = w[:-1]

            if not w:
                for remaining in l['R']:
                    if remaining == remaining[::-1]:
                        answers.append([self.travel(l, remaining), i])
            
            w = words[i][::-1]
            l = rev_charmap
            while w:
                if '@' in l and w == w[::-1]:
                    answers.append([l['@'], i])

                c = w[-1]

                if c in l:
                    l = l[c]
                else:
                    break
                w = w[:-1]

            if not w:
                for remaining in l['R']:
                    if remaining == remaining[::-1]:
                        answers.append([self.travel(l, remaining), i])

            l = charmap
            w = words[i]
            for j in range(len(w)):
                c = w[j]
                if c not in l:
                    l[c] = {'R': []}
                l[c]['R'].append(w[j+1:])
                l = l[c]
            l['@'] = i

            l = rev_charmap
            w = words[i][::-1]
            for j in range(len(w)):
                c = w[j]
                if c not in l:
                    l[c] = {'R': []}
                l[c]['R'].append(w[j+1:])
                l = l[c]
            l['@'] = i
        return answers

s = Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]),'|', [[0,1],[1,0],[3,2],[2,4]]) 
print(s.palindromePairs(["bat","tab","cat"]),'|', [[0,1],[1,0]])
print(s.palindromePairs(["a", ""]),'|', [[0,1],[1,0]])