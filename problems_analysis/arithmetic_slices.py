"""
The naive way would be start at each number n and
then iterate until you no longer find a sequence.

Runtime: O(n^2) ; Space: O(1)
"""

"""
I didn't use the naive solution, but what I saw was
that you can use dp / memory to see what the previous 
calculations were because you need numbers in sequences
which means that the only number that matters if the 
previous one. With the figured out, I saw that you're
really counting the numbers sequentially. What this means
is that a sequence of 3 numbers gives you 1 combination,
4 - 2 extra combinations (in addition to the 1), 5
3 extra combinations (in addition to the 2 and 1), so it
builds up from there.

As a result you only need to save what the prev diff was
and what the count of it was and then sum up the count.

Also, what I found out was that iterating forward saves
a more memory in python which is due to how the for loop
works when you're iterating reversely apparently. Maybe,
it first creates the forward arary of numbers and then
it reverses it.

Runtime: O(n) ; Space O(1)
"""