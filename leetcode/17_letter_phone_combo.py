class Solution:
    def letterCombinations(self, digits):
        key = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wyxz"
        }

        temp = []
        

        for i in range(len(digits)):
            num = digits[i]
            letters = key[num]

            if i == 0:
                for j in letters:
                    temp.append(j)
            else:
                new_temp = []
                for old_str in temp:
                    for k in letters:
                        new_temp.append(old_str + k)
                temp = new_temp
        return temp

s = Solution()
print(s.letterCombinations("4214"))

            

