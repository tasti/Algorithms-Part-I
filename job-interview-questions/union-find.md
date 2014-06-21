Interview Questions: Union-Find
===============================

Question 1
----------

**Social network connectivity.** Given a social network containing N members and a log file containing M timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be MlogN or better and use extra space proportional to N.

Answer 1
--------

Solution: union-find/q1.py

Input: union-find/q1.in

The first line gives the number of test cases, **C**. **C** test cases follow. Each test case starts with a line containing a single integer **N**, the number of members in the social network. Next follows a line containing a single integer **M**, the number of formed friendships. **M** lines follow containing three space-separated integers: **A**, **B** and **T**. **A** and **B** represent the unique ID of a member in the social network (unique IDs range from **0** to **N-1**). **T** represents the timestamp at which **A** and **B** formed a friendship.

Output: union-find/q1.out

For each test case, a line contains the earliest time at which all members are connected or **"Never"** if there is no point at which all members are connected..

Question 2
----------

**Union-find with specific canonical element.** Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component containing i. The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find() method should return 9 for each of the four elements in the connected components.

Answer 2
--------

Solution: union-find/q2.py

Question 3
----------

**Successor with delete.** Given a set of N integers S={0,1,...,N−1} and a sequence of requests of the following form:
Remove x from S
Find the successor of x: the smallest y in S such that y≥x.
design a data type so that all operations (except construction) should take logarithmic time or better.

Answer 3
--------

...

Question 4
----------

**Union-by-size.** Develop a union-find implementation that uses the same basic strategy as weighted quick-union but keeps track of tree height and always links the shorter tree to the taller one. Prove a lgN upper bound on the height of the trees for N sites with your algorithm.

Answer 4
--------

Solution: union-find/q4.py
