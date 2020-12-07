class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        l = preorder.split(",")
        i = 0
        n = 1
        child = 0
        for i in range(len(l)):
            if n == 0:
                if child == 0:
                    return False
                n = child
                child = 0
                
            if l[i] != '#':
                child += 2
            n -= 1
        if n != 0 or child != 0:
            return False
        return True


s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"), True)
print(s.isValidSerialization("1,#"), False)
print(s.isValidSerialization("9,#,#,1"), False)
print(s.isValidSerialization("#"), True)