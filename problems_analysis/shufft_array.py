"""
I need a way to shuffle the indices in the array using
in a way ideally with cosntant space. With space,
what would this look like? You would need a data
structure that you could randomize but also but able
to pop or shorten at the same time.

The way that I thought of was that instead you could
just simply randomize what numbers you want to exchange
in that array. To do so for a completely random shuffle,
you would iterate through the indices and then get a random
index and switch the values between them.

Runtime: O(n) ; Space:  O(n) - for initial setup
"""