Interview Questions: Analysis of Algorithms
===========================================

Question 1
----------

**3-SUM in quadratic time.** Design an algorithm for the 3-SUM problem that takes time proportional to N<sup>2</sup> in the worst case. You may assume that you can sort the N integers in time proportional to N<sup>2</sup> or better.

Answer 1
--------

Solution: analysis-of-algorithms/q1.py

Question 2
----------

**Search in a bitonic array.** An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing sequence of integers. Write a program that, given a bitonic array of N distinct integer values, determines whether a given integer is in the array.
- Standard version: Use ∼3lgN compares in the worst case.
- Signing bonus: Use ∼2lgN compares in the worst case (and prove that no algorithm can guarantee to perform fewer than ∼2lgN compares in the worst case).

Answer 2
--------

...

Question 3
----------

**Egg drop.** Suppose that you have an N-story building and plenty of eggs. An egg breaks if it is dropped from floor T or higher and does not break otherwise. Your goal is to devise a strategy to determine the value of T given the following limitations on the number of eggs and tosses:
- Version 0: 1 egg, ≤T tosses.
- Version 1: ∼1lgN eggs and ∼1lgN tosses.
- Version 2: ∼lgT eggs and ∼2lgT tosses.
- Version 3: 2 eggs and ∼2sqrt(N) tosses.
- Version 4: 2 eggs and ≤csqrt(T) tosses for some fixed constant c.

Answer 3
--------

...
