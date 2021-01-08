"""
Brute Force
Try every single combination at each i
Runtime : O(n^2); Space O(1)
"""

"""
In Brute Force, you can see that you don't need to look
at numbers with a lower height than i. This is related to
the iterated /moving number.

In the non-moving number, i, which is moved from one number
to another in the outer loop, but no in the inner, what you're
really hoping to hold is the furtherest to the left or right number
that will be bigger or equal to the number at i.

Thus, you can hold a variable for the two pointers (left and right)
and also sort the numbers so that you can ensure that all the numbers
at i will have left and right pointers be larger than the number at i.
"""