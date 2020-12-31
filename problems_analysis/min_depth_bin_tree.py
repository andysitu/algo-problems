"""
Similar to the max depth bin tree except you are taking
the minimum instead of the max. If you find the depth of
the left child, then you can start the calculation of  the
right child if it exceeds that min depth or vice versa.
This would require the recursive approach.

Runtime O(n) ; Space O(n)/O(1) depending on how recursion is seen
"""

"""
Another approach is to only explore the node with the min depth.
This way, as soon as you approach the first leaf node, it would be
the minimal height. A queue would work with a fifo approach while

If it's a balanced tree, then you would have to approach all the nodes,
but any approach would have to do so anyway if you want to explore
the entirety of the nodes and ensure correctness.
"""