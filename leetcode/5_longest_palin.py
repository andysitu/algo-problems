def longestPalindrome(s):
    start_points = {}
    ls = len(s)

    for i in range(ls):
        if (i+1 < ls and s[i] == s[i+1]):
            start_points[str(i) + "_2"] = [i,i+1]
        if (i+2 < ls and s[i] == s[i+2]):
            start_points[str(i) + "_3"] = [i,i+2]
    max_length = -1
    max_sa = 0
    max_sb = 0
    for i in start_points:
        sa = start_points[i][0]
        sb = start_points[i][1]
        while (sa - 1 >= 0 and sb + 1 < ls and s[sa-1] == s[sb+1]):
            sa -= 1
            sb += 1
        if (sb-sa)> max_length:
            max_sa = sa
            max_sb = sb
            max_length = sb-sa
    return s[max_sa: max_sb + 1]

print(longestPalindrome("aaaa"))

    