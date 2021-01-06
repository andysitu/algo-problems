"""
Brute Force
At every character of the string, iterate the
rest of the characters until you see a repeated char.
Then, record that as the max
Runtime: O(n^2) ; Space O(1)
"""

"""
DP
You can save the characters you've seen so far and
then calculate in constant time if you do see the
repeated characters of what the count will be if you
skip the previous character instead.

I didn't account for the fact that the previous character
may be before the last repeated character so there needs
to be a variable that records the last index of the 
repeated character.

Runtime: O(n) ; Space: O(1)
"""