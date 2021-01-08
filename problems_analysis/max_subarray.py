"""
Brute Force
For each n in the array, add the numbers from i+1 until the
end of the array while recording the max number encountered
O(n^2) ; Space O(n)
"""

"""
Getting only larger numbers
From the brute force appraoch, one can see a pattern emerge
where there are numerous calculations that are repeated.

You can start from one side of the array and either take the
current number or take the current number and the previous number.
In other words, the maximum sum. Also, record the maximum
num encountered.

Runtime O(n) ; Space O(1)
"""

"""
DP
If i-1 is >0, then add [i] and [i-1] number, else just have [i]
This is the same as the previous approach but it would take space O(n)
"""

"""
Divide and conquer
break the array in smaller fragments until you reach length 2 and then
build up recursively. Once the smaller fragments are reached, if
right is greater than left, then return left + right. Else, return 
number, and so forth.

On further though, you would have to do the same from the right side,
and you would use the recusion to really find any larger number than
the on that you're lookin at since you at the mid point, you have to travel
left and travel to get the largest number.

As a result, it's not faster in runtime, and I believe it's in nln time.

Runtime: O(nln(n))
"""