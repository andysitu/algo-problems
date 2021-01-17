"""
The divide and conquer sorting algorithms essentially will
iterate a process that fulfills this, where you have
to navigate through all the numbers and divide them
between the greater and lesser numbers. As a result, the
quick sort algorithm fulfills this perfectly, where at
the first iteration, you will have the pivot or partition
and you have the lesser numbers and greater numbers. This gives
you a total count of the numbers in each group, and as a result,
you then have to either chose the lesser batch or the greater 
batch.

At each new batch, you can start with an existing count and
then work from there. Finally, if you find a number k as
the pivot point, then you return this number.

In theory, by randomizing the index at which you pivot, then
over a large quanitty of numbers and iterations, you will run
into the average case, which is having half greater and half lesser.
This means a runtime of O(nlnn).
"""