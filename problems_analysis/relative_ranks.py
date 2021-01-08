"""
The brute force method is to hold an inrement variable and then
search through the numbers repeated to find the next largest
number

Runtime O(n^2) Space O(1) or O(n) for the returned array
"""

"""
Sort
Sort the numbers and then pull their indices and values using
a dictionary.

To save space, modify the number array given 

Runtime O(nln n) Space O(n) for the returned array
"""

"""
I was stuck for a long time tring to find an error that was
due to having duplicates in my test cases.

I couldn't think of anything that could beat the runtime
since you should have to sort everything in order to get the rank.
Bin sort would be O(n) but I couldn't think of how to apply it in
this case. 

Space might be a consideration.
"""