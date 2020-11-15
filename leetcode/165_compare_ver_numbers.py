class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vlist1 = version1.split('.')
        vlist2 = version2.split('.')

        end = max(len(vlist1), len(vlist2))
        v1, v2 = None,None

        for i in range(end):
            if i >= len(vlist1):
                if int(vlist2[i]) == 0:
                    continue
                return -1
            if i >= len(vlist2):
                if int(vlist1[i]) == 0:
                    continue
                return 1

            v1 = int(vlist1[i])
            v2 = int(vlist2[i])
            if v1 > v2:
                return 1
            elif v2 > v1:
                return -1
        return 0