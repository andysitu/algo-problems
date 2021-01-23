"""
I knew that you need something like a set to be able to
retrieve the values instantly but also something like an
array so that you an get any value randomly via the index.
My initial thoughts were to somehow find a data structure
that had both of these elements.

After some, I figured that I could have a set, dictionary,
and array that would have the indices and values, but upon
further thought you wouldn't need a set. You only need
a dictionary that would contain the indices for the list and 
then the list to retrieve the values randomly. A list works
best by appending and removing values using the pop
and append operation as this would amoritized its operation
to O(1) and this can be done by always switching the value
with the last element in the array.

Runtime: O(1) ; Space: O(n)
"""