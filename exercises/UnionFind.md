Union Find
==========

To specify an array or sequence of values in an answer, separate the values in
the sequence by whitespace. For example, if the question asks for the first
ten powers of two (starting at 1), then the following answer is acceptable:

     1 2 4 8 16 32 64 128 256 512

If you wish to discuss a particular question and answer in the forums, please post
the entire question and answer, including the seed (which can be used by the course
staff to uniquely identify the question) and the explanation (which contains the
correct answer).

Question 1
----------

(seed = 501381)
Give the id[] array that results from the following sequence of 6 union
operations on a set of 10 items using the quick-find algorithm.

    6-2 7-4 3-0 3-6 9-1 9-7

Recall: our quick-find convention for the union operation p-q is to change id[p]
(and perhaps some other entries) but not id[q].

Answer 1
--------

    2 4 2 2 4 5 2 4 8 4

Question 2
----------

(seed = 618811)
Give the id[] array that results from the following sequence of 9 union
operations on a set of 10 items using the weighted quick-union algorithm from lecture.

    2-8 8-9 1-4 7-8 7-0 3-6 1-3 2-3 5-6

Recall: when joining two trees of equal size, our weighted quick union convention is to
make the root of the second tree point to the root of the first tree. Also, our weighted
quick union algorithm uses union by size (number of nodes), not union by height.

Answer 2
--------

    2 2 2 1 1 2 3 2 2 2

Question 3
----------

(seed = 860081)
Which of the following id[] array(s) could be the result of running the weighted quick union
algorithm on a set of 10 items? Check all that apply.

Answer 3
--------

- [ ] 6 6 1 7 6 7 7 2 7 7 
- [x] 3 3 3 3 7 3 3 0 0 3
- [ ] 6 0 0 0 0 7 6 0 8 5 
- [ ] 9 6 7 5 7 1 6 1 1 1 
- [x] 0 7 2 6 4 6 6 7 8 9
