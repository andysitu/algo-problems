"""
The brute force way would be calculate every single
possible iteratively in 4 for loops with a counter.

Runtime: O(n^4) ; Space O(1)
"""

"""
The only other option that I could think of was to 
calculate 2 of the lists out for all sum combinations
and then calculate the other half as well and then
save the count of their sums in a hash map.

Finally, you would compare all the values in the hash
map and calculate the counter values
eg dict 1 has count of 10 for -1 and dict 2 has a count
of 20 for 1, then the sum of that would be 10 * 20 = 200.

Checkinig the values in the hashmap is constant and it
cuts the calculations by a significant margin
Runtime: Potentially O(n^4) ; Space O(n^2)

It didn't occur to me the comparisons of the two dictionaries
could be very messy but luckily I didn't have to implement this.
"""

"""
In writing the code, I saw that you don't need the second
dictionary since in doing the second round of calculations
with the last 2 lists, you can simply check if the negative value
exists in the first dictionary and simply add that count
to the sum.

Runtime: O(n^2) : Space: O(n^2)
""