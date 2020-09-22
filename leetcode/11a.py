class Solution:
    def maxArea(self, height):
        max_len = len(height)
        temp_area = 0
        n1 = 0
        sorted_index = sorted(range(max_len), key=lambda k: height[k])
        count = 0
        x = 0
        max_area = 0
        
        a = 0
        b = max_len - 1
        va = height[a]
        vb = height[b]


        def calculate_area(a, b):
            if a > b:
                temp = a
                a = b
                b = temp
            v1 = height[a]
            v2 = height[b]
            if v1 > v2:
                return v2 * (b-a)
            else:
                return v1 * (b-a)

        while True:
            if a + 1 >= b:
                break
            temp_area = calculate_area(a + 1, b)
            if temp_area > max_area:
                a += 1
                max_area = temp_area
                continue

            temp_area = calculate_area(a, b-1)
            if temp_area > max_area:
                b -= 1
                max_area = temp_area
                continue
            break
        
        for a in range(max_len-1, -1, -1):
            i = sorted_index[a]
            
            n1 = height[i]
            if n1 * max_len-1-i > max_area or n1 * i > max_area:
                count += 1
                for b in range(a+1, max_len):
                    x += 1
                    j = sorted_index[b]
                    if j>i:
                        diff = j - i
                    else:
                        diff = i - j
                    temp_area = n1 * diff
                    if temp_area > max_area:
                        max_area = temp_area
        print(count, x)
        return max_area