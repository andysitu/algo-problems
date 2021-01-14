def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest_len = 0
    cur_len = 0
    input_keys = {}
    i = 0
    while i < len(s):
        if s[i] not in input_keys:
            cur_len += 1
            if cur_len > longest_len:
                longest_len = cur_len
            input_keys[s[i]] = i
        else:
            cur_len = 0
            i = input_keys[s[i]]
            input_keys = {}
        i += 1
    return longest_len