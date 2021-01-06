"""
DFS
First and only solution that I can think up: have an
array of the dependencies with index being the current
course that is dependent on another and then the array
values being the courses that need to be taken before
this course. Then, an array that records whether there
is a cycle in the route that will be travelled or if 
route will be okay. Else if it hasn't been travelled
then it will be equal to 0.

As a result, for each course number you will travel
through its routes, but this will be fast because the
array has already saved any previous travelled routes.

Also, recursion will be used to travel through the routes.

Runtime: O(n + d) ; Space(n + d) with d being # of dependencies
"""

"""
Instead of using recursion, you can also use a queue/stack to contain
the routes that must be travelled in order

Queue would be BFS and stack would be DFS. In BFS, it would be nearly
the same, except you would have to travel all routes in
a single node at a time so that you can mark that node as travelled.
"""