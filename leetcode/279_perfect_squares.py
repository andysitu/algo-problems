import queue

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        squares = []
        si = 1
        s = 1
        q = queue.Queue()
        ndict = {}
        squares = []
        while s <= n:
            if s == n:
                return 1
            squares.append(s)
            # q.put((s,1))
            si += 1
            s = si ** 2

            
        squarelen = len(squares)
        for i in range(squarelen-1, -1, -1):
            q.put((squares[i], 1))
        
        while not q.empty():
            t = q.get()
            if t[0] in ndict:
                continue
            if n-t[0] in ndict:
                return t[1] + ndict[n-t[0]]
            for i in range(squarelen-1, -1, -1):
                nsum = t[0] + squares[i]
                if nsum == n:
                    return t[1] + 1
                elif nsum > n:
                    continue
                else:
                    q.put((nsum, t[1] + 1))
            ndict[t[0]] = t[1]

s = Solution()
print(s.numSquares(42331))
print(s.numSquares(12))
