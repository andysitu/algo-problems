"""
Use recursion to travel through all the islands. Initially
I tried to use an array to hold values to travel but then
in one of the tests cases where I got it wrong I realized 
that it wouldn't be able to travel in the provinces that
were out of order due to how it was iterated.

As as a result, I used recursion to travel through the
provinces. At worst case it will be runtime O(n^2) where
all the cities are their own pronvince, and at best case
it still would be runtime n^2 since in each new city
you need to explore all the links that it may have.

Essentially, this is DFS. I belive you would need to have
a runtime similar to this since you need to explore all
the links that might be possibly connected. You might
be able to cut out half of the connections since 
[i][j] is equal to [j][i], but O is still the same.
"""