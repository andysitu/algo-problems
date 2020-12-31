"""
Using the aproach in the max depth of the binary tree problem
of the recursion and queue/ stack (stack for DFS), the best
approach boils down to type of trees that would be seen.

If the width is greater than the depth, then DFS might be
better since it will explore depth first. On the other hand,
BFS would be faster if the tree does have plenty of early
root nodes.

By iterating through the nodes, you can also compare it with
the height of one child and then compare it with the other if
it exists.
"""