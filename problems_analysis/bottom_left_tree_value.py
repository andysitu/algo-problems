"""
My logic was that you have to travel through every single
node because you don't have a logical, systemicatic way
of finding the lowest node without having travelled through
it. Thus, an O(n) solution is good enough.

This meant that using recursion should be good enough, and
if you travel through the left node first, the recursion
will make it so that you will always approach the left most
node first of that value so by saving the max level
and max value, you can guarantee that you will always record
the left most bottom node.

Runtime: O(n) ; Space: O(n) depending on how recursion is viewed
"""

"""
To my surprise, using a stack to the nodes is faster and saves a
lot more space than the recursive method. This might be because of
the space and time it takes to start each new function call, but
the stack means that you have to keep O(n) nodes since for every
node that you take out of the stack, you potentially put 2 more.

To guarantee traversal of left node first, you put right node
onto the stack first.

Runtime: O(n) ; Space O(n)
"""