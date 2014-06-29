Interview Questions: Elementary Sorts
=====================================

Question 1
----------

**Intersection of two sets.** Given two arrays a[] and b[], each containing N distinct 2D points in the plane, design a subquadratic algorithm to count the number of points that are contained both in array a[] and array b[].

Answer 1
--------

Solution: elementary-sorts/q1.py

2D points on a plane are represented as a 2-element array (i.e. [x, y]).

Question 2
----------

**Permutation.** Given two integer arrays of size N, design a subquadratic algorithm to determine whether one is a permutation of the other. That is, do they contain exactly the same entries but, possibly, in a different order.

Answer 2
--------

Solution: elementary-sorts/q2.py

Question 3
----------

**Dutch national flag.** Given an array of N buckets, each containing a red, white, or blue pebble, sort them by color. The allowed operations are:
 - swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
 - color(i): color of pebble in bucket i.
The performance requirements are as follows:
 - At most N calls to color().
 - At most N calls to swap().
 - Constant extra space.

Answer 3
--------

Solution: elementary-sorts/q3.py