class Solution:
    def countBits(self, num: int) -> List[int]:
        a = [0]
        if num == 0:
            return a
        n = 0
        bit = 2
        index = -1
        
        for i in range(1, num+1):
            if i == bit:
                bit *= 2
                a.append(1)
                index = 0
                continue
            index += 1
            a.append(a[index]+1)
        return a
            