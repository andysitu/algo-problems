from typing import List

class Solution:
    ips = []

    def check_str(self, s, start, end):
        nstr = s[start:end]
        slen = len(nstr)
        n = int(nstr)
        if n > 255:
            return False
        elif nstr[0] == '0' and slen > 1:
            return False
        else:
            return True

    def create_ip(self, s, l1, l2, l3, l4):
        end2 = l1+l2
        end3 = l1+l2+l3
        end4 = l1+l2+l3+l4
        slen = len(s)
        if l4:
            if slen == end4:
                if self.check_str(s, end3, end4):
                    self.ips.append(s[:l1] + "." + s[l1:l1+l2] + "." + s[l1+l2:l1+l2+l3] + "." + s[l1+l2+l3:l1+l2+l3+l4])
        elif l3:
            if 1 <= slen - (end3) <= 3 and self.check_str(s, end2, end3):
                self.create_ip(s, l1, l2, l3, 1)
                self.create_ip(s, l1, l2, l3, 2)
                self.create_ip(s, l1, l2, l3, 3)
        elif l2:
            if 2 <= slen - (end2) <= 6 and self.check_str(s, l1, end2):
                self.create_ip(s, l1, l2, 1, 0)
                self.create_ip(s, l1, l2, 2, 0)
                self.create_ip(s, l1, l2, 3, 0)
        elif l1:
            if 3 <= slen - (l1) <= 9 and self.check_str(s, 0, l1):
                self.create_ip(s, l1, 1, 0, 0)
                self.create_ip(s, l1, 2, 0, 0)
                self.create_ip(s, l1, 3, 0, 0)
        else:
            if 4 <= slen <= 12:
                self.create_ip(s, 1, 0, 0, 0)
                self.create_ip(s, 2, 0, 0, 0)
                self.create_ip(s, 3, 0, 0, 0)
        return False

    def restoreIpAddresses(self, s: str) -> List[str]:
        slen = len(s)
        self.ips.clear()
        self.create_ip(s, 0, 0, 0, 0)
        return self.ips

s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("234245109"))
print(s.restoreIpAddresses("222"))
print(s.restoreIpAddresses("2223"))
print(s.restoreIpAddresses("010101"))
print(s.restoreIpAddresses("032"))
print(s.restoreIpAddresses("9999"))
print(s.restoreIpAddresses("99999999999"))
print(s.restoreIpAddresses("9999999999"))
print(s.restoreIpAddresses("999999999"))
print(s.restoreIpAddresses("99999999"))