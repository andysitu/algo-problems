"""
This is similar to problem 387 except it has duplicate values.
I didn't know that heap and priority queue for Python had
this issue so you need to write an __lt__ function in a new
class or as I found later just modify the __lt__ of the
ListNode class directly.

Runtime: O(nlnn) ; Space: (n)
"""