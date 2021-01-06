"""
Brute Force
At each i, get the longest string possible
O(n^2) ; Space O(1)
"""

"""
Attempt
Save chars in a dict of lists. Then, calculate the max size
and the length of the list and the start and end indices.

The calculation was too complicated, though it seems that it
will work eventully albeit slowly.

Space O(n)
"""

"""
Instead save the counts of the characters in a list of length 26.
Then, record the start variable for each char and manually
increase the starts as you go down the less and find that
current_index - start +1 - count[c] > k. You increment start
and then decrease the count[c] if chars are encountered

The runtime is potentially O(n^2), but should work
"""

"""
The only thing that matters the is the maximum output so if you record
the count in the equation seen previously as the maximum count that you've
seen so far, then you decrease the calculations need and then you can
decrease any characters that you encounter as you increment start
because only the maximum value matters.

Runtime: O(n) ; Space O(1)
"""

"""
The space and runtime decreases if you use a dictionary instead for python.
You no longer have to calculate the char as an integer value using ord 
and you can directly plug it into the dictionary with char properties.
Also, you won't always need 26 cells for all the characters.
"""