from typing import List
import sys

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        zeroes = 0
        negbits, posbits = 0, 0

        for n in nums:
            if n > 0:
                posbits ^= n
            elif n < 0:
                negbits ^= -n
            else:
                print(0)
                zeroes += 1
        if zeroes == 1:
            if posbits > 0:
                return [0, posbits]
            else:
                return [0, -negbits]
        elif posbits > 0 and negbits > 0:
            return [posbits, -negbits]
        elif posbits > 0: # only positive
            # find bit that is 1 (diff betw the two numbers)
            bbin = bin(posbits)
            for i in range(len(bbin)-1, 1, -1):
                if bbin[i] == '1':
                    findbit = 2**(len(bbin) - i - 1)
                    break
            zerobitxors = 0
            onebitxors = 0
            for n in nums:
                if n & findbit > 0:
                    onebitxors ^= n
                else:
                    zerobitxors ^= n
            return [zerobitxors, onebitxors]
        else: # only negatives
            bbin = bin(negbits)
            for i in range(len(bbin)-1, 2, -1):
                if bbin[i] == '1':
                    findbit = 2**(len(bbin) - i - 1)
                    break
            zerobitxors = 0
            onebitxors = 0
            for n in nums:
                if n > 0:
                    continue
                if -n & findbit > 0:
                    onebitxors ^= -n
                else:
                    zerobitxors ^= -n
            return [-zerobitxors, -onebitxors]

s = Solution()
# print(s.singleNumber([1, 3, 4, 5, 4, 3, 1, 9]), [5,9])
# print(s.singleNumber([1,2,1,3,2,5]), [3,5])
# print(s.singleNumber([1,2,1,3,2,5,3,0]), [0,5])
# print(s.singleNumber([1,2,1,3,-4,2,5,3,0,5]), [0,-4])
# print(s.singleNumber([1,2,0,1,3,2,5,3,0,-4]), [-4,5])
# print(s.singleNumber([-6,-7,-8,-9,-5,-6,-7,-8]), [-9,-5])
# print(s.singleNumber([-6,-7,5,100,100,-8,-9,-5,-6,4,5,-7,-8,4]), [-9,-5])
# print(s.singleNumber([-6,-7,5,100,62,100,-8,-9,-5,-6,4,5,-7,-8,4,-5,12,-9,48,12,48,41]), [62,41])
# print(s.singleNumber([62,-6,-7,5,100,62,100,-8,-9,-5,-6,4,-210,5,-7,41,-101,-8,4,-5,12,-9,48,12,48,41]), [-210,-101])

slist = [-2017078396,1427014140,987529319,-277720653,-901501327,461557219,1531771710,-486222465,1065241267,-150752724,279065789,-979167287,-2129000919,351169793,987529319,1291943415,-1198652495,-1390807232,-1384211381,1427014140,-1698470425,-1698470425,-703318677,-1586850882,1355734673,734734207,279065789,-407414062,552520367,-1634507058,-1390807232,-1171102957,-2017078396,813133369,2018595612,1203433967,-1634507058,-1722143339,552520367,83097707,-210227883,-1334100211,1266014339,431255111,431255111,1487644701,2043227115,-901501327,-1685439676,-2129000919,407483519,-407414062,-1284422899,-1284422899,734734207,-703318677,1865535261,-1685439676,407483519,-210227883,1355734673,1754381294,1065241267,1801796253,1531771710,461557219,-1198652495,2018595612,-232685875,-1655623443,1217074301,-950274679,83097707,-277720653,1291943415,-1705853183,-2003029055,-1334100211,-150752724,1217074301,-979167287,1266014339,-1384211381,-232685875,813133369,1203433967,-2003029055,-1705853183,1754381294,1707386140,2043227115,1801796253,-1655623443,1660957712,-486222465,351169793,1487644701,-950274679,1865535261,-1586850882,1707386140,-1171102957]

print(s.singleNumber(slist), [-1722143339,1660957712])