"""
First iterate  through the string and keep a count
of all the characters.

Then, iterate it again and return the first char
that has a count of 1.

Runtime is O(n) and I don't think there is any
way to get it faster than running it at least once
in order to see all the chars that you have.

The second iteration you might be able to save some steps
by iterating through the counter instead of the string if it
is able to record the order which the characters were added to it
and then  you will at most run it 26 times, and I believe that
python does this in the newer version.

Weirdly enough, it runs slower than iterating it through the string
twice, so it depends on the run cases.
"""

"""
Running collections.Counter is much faster as it is an internal
python data structure that does the counting much better.
"""