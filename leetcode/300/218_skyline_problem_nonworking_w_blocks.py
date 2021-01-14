from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if (len(buildings)) == 0:
            return []
        blocks = []
        block = None
        l, r = 0, 0
        for i in range(0, len(buildings)):
            b = buildings[i]
            bl, br, bh = b[0], b[1], b[2]

            if block == None or bl > r:
                # sort previous block's points
                if block != None:
                    block["points"].sort(key=lambda p: p[0])
                    block["start"] = len(block["points"]) - 1
                # new block
                block = {}
                block["points"] = []
                block["buildings"] = []
                l, r = bl, br
                blocks.append(block)            
            if br > r:
                r = br
            block["points"].append((bl, bh, bh))
            block["points"].append((br, bh, bh))
            block["buildings"].append(i)

        block["points"].sort(key=lambda p: p[0])
        block["start"] = len(block["points"]) - 1
        # print(blocks)

        # remove points dwarfed by other buildings
        for block in blocks:
            for i in range(len(block["buildings"])-1, -1, -1):
                b = buildings[block["buildings"][i]]
                for j in range(block["start"], -1, -1):
                    p = block["points"][j]
                    if b[0] <= p[0] <= b[1] and b[2] > p[1]:
                        del block["points"][j]
                        block["start"] -= 1
                    elif b[1] < p[0]:
                        block["start"] = j - 1
        print(blocks)
        a = []
        prev=None
        for block in blocks:
            plen = len(block["points"])
            for i in range(plen):
                if i == plen - 1:
                    a.append([block["points"][i][0], 0])
                    prev = None
                elif i == 0:
                    prev=[block["points"][i][0], block["points"][i][1]]
                    a.append(prev)
                else:
                    n=[block["points"][i][0], block["points"][i+1][1]]
                    if prev != None and n[1] == prev[1]:
                        continue
                    a.append(n)
                    prev = n
        return a


s = Solution()
print(s.getSkyline([[2,9,10],[2,20,3],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[0,1,3]]))
# print(s.getSkyline([[0,2,3],[2,5,3]]))