class Solution:
    def maxArea(self, height):
        max_area = 0
        max_len = len(height)
        calc_area = 0
        n1 = 0 
        n2 = 0

        sorted_index = sorted(range(max_len), key=lambda k: height[k])
        count = 0
        b = 0
        c = 0
        
        for a in range(max_len-1, -1, -1):
            i = sorted_index[a]
            
            n1 = height[i]
            if n1 * max_len-1-i > max_area:
                count += 1
                for j in range(0, i):
                    b += 1
                    n2 = height[j]
                    if (n2 >= n1):
                        calc_area = n1 * (i-j)
                        if calc_area > max_area:
                            max_area = calc_area
                        break
            if n1 * i > max_area:
                
                for j in range(max_len-1, i, -1):
                    c += 1
                    n2 = height[j]
                    if (n2 >= n1):
                        calc_area = n1 * (j-i)
                        if calc_area > max_area:
                            max_area = calc_area
                        break
            else:
                break
        print(count, b, c)
        return max_area