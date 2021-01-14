class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hmin = 0
        if len(citations) == 0:
            return 0
        hcurrent = citations[len(citations)-1]
        htotal = 0
        for i in range(len(citations)-1, -1, -1):
            if hmin > citations[i]:
                return hmin
            hcurrent = min(hcurrent, citations[i])
            htotal += 1
            
            if hcurrent <= htotal:
                return hcurrent
            hmin = max(hmin, min(htotal, hcurrent))
        return hmin