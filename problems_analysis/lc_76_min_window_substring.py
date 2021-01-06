"""
The only solution that I could come up with is to  use
the sliding window. First create a dictionary of the
characters required with the values being the number
of characters that have to be seen in the large string s

Next, iterate through s at i and have a start variable.
At each character in s, decrease the cont in the dict
And see if you can increment s if the char at s is not
in the dict (thus not in the to be replaced string t)
or if the dict value at that char is lower than 0 (thus
meaning there are extra chars). Keep on incrementing
until these conditions are met. 

Finally at the end of these, check if all the chars have
been replaced. If so, then record the min len of 
i - start + 1.

Runtime: O(n) ; Space O(1)
"""

"""
Initially I had iterated through the dictionary counter each
time to make sure that the values were all 0 or lower.

I drastically decreased the time by just having a counter
of the amount of chars taht have to be replaced and this 
counter decreased only in the correct conditions.
"""