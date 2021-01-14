"""
This is related to Project Euler's problem 24, which also
sort of corresponds to lc's problem 46.

I was thinking of two solutions that would both require space
and subsequently time since you'd be generating all combinations

Generating the combinations by removing the numbers already used.
This is actually backtracking where you have an array of numbers
and then you iterate through all the possible numbers, remove that
from the candidates, and then add it to the path that you currently
are on. Finally, your final answer at the end will be added
to the output. This takes an enormous amount of space since each
recursive function will branch to more functions and each function
requires its own combination of numbers and path.

Insertion of the numbers by using previous combinations of generated
numbers. This will be started at index 0 starting from the right
and then you move to the next number with the numbers generated at
the previous iteration (that wouldn't include the current number).
The numbers are iterated in order (thus smallest to largest) and in
this way you are generating the numbers in order.
"""

"""
Both requires at least space O(n!) and the runtime is similar depending
on  the implemenation. That's because there are this many combinations.

A better approach depending on the problem would be to do this iteratively
if it only asks for the number at X such as the one in project euler, but
I haven't been able to think of solution as it gets too convoluted for me.

One way would to be just cut off the combionations as soon as the length
is enough for the output as it was described previously.
"""