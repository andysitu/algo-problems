class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        nlen = len(intervals)

        if nlen == 0:
            return [newInterval]
        l = newInterval[0]
        r = newInterval[1]

        values = []
        left = right = -1
        placed = False

        if r < intervals[0][0]:
            right = r
            left = l
            values.append([left, right])
            placed = True
        elif l < intervals[0][0]:
            left = l
                
        for i in range(nlen):
            n = intervals[i]
            if left == -1:
                if l < n[0] and i > 0 and l > intervals[i-1][1]:
                    left = l
                elif l >= n[0] and l <= n[1]:
                    left = n[0]
                    print(left)
                
            if right == -1:
                if r < n[0] and i > 0 and r > intervals[i-1][1]:
                    right = r
                    values.append([left, right])
                    values.append(n)
                    placed = True
                    continue
                elif r >= n[0] and r <= n[1]:
                    right = n[1]
                    values.append([left, right])
                    placed = True
                    continue

            if (left == -1 and right == -1) or (left != -1 and right != -1):
                values.append(n)
        if not placed:
            if left == -1:
                left = l
            if right == -1:
                right = r
            values.append([left, right])
        
        return values