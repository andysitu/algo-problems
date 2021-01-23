"""
The brute force way would be to test every single possibility
of every string out.

Runtime: O(n^2) ; Space O(1)
"""
"""
Divid & Conquer
I believe that this is the divide and conquer approach.
You first count all the characters in a string and then
you iterate through it again except this time you will
break the string via their indices and recursion every
time you encounter a character with a count lower k.

These characters are definitely no good and you need
to work around them. I run into a typo where you need
a variable that will record the start of where you
want the recursion to begin, but I mistakenly set it
to 0.

The worst case of O(n^2) when you need a split at every
single character  so that it would occur n times
for n layers.

Space: Each call builds a total stack of n size for each
layer so it's similar to the runtime complexity. 
"""