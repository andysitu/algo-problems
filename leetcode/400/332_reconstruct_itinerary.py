from typing import List

class Solution:
    def travel(self, loc, dictA, path, count, finalcount):
        if count == finalcount:
            return path + [loc]
        if loc not in dictA:
            return False
        for i in range( len(dictA[loc]) ):
            if dictA[loc][i] ==  'X':
                continue
            v = dictA[loc][i]
            dictA[loc][i] = 'X'
            result = self.travel(v, dictA, path + [loc], count+1, finalcount)
            if result == False:
                dictA[loc][i] = v
            else:
                return result
        return False
                
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dictA = {}

        for t in sorted(tickets):
            if t[0] not in dictA:
                dictA[t[0]] = []
            dictA[t[0]].append(t[1])
        
        return self.travel("JFK", dictA, [], 0, len(tickets))

s = Solution()
# print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))