Quicksort
=========

To specify an array or sequence of values in an answer, separate the values in
the sequence by whitespace. For example, if the question asks for the first
ten powers of two (starting at 1), then the following answer is acceptable:

     1 2 4 8 16 32 64 128 256 512

If you wish to discuss a particular question and answer in the forums, please
post the entire question and answer, including the seed (which can be used by
the course staff to uniquely identify the question) and the explanation (which
contains the correct answer).

Question 1
----------

(seed = 23535)
Give the array that results after applying the standard 2-way partitioning
algorithm from lecture to the following array:

    63 31 71 96 82 93 37 50 46 29 55 52

Recall, in the standard 2-way partitioning algorithm, the leftmost entry is the partitioning item.

Answer 1
--------

50 31 52 55 29 46 37 63 93 82 96 71

Question 2
----------

(seed = 474174)
Give the array that results after applying Dijkstra's 3-way partitioning
algorithm from lecture to the following array:

    41 94 41 73 41 96 17 13 29 58

Answer 2
--------

29 13 17 41 41 41 96 73 58 94

Questions 3
-----------

(seed = 273826)
Which of the following statements about quicksort are true? Check all that apply. Unless otherwise specified, assume that quicksort refers to the recursive, randomized version of quicksort (with no extra optimizations) and uses the 2-way partitioning algorithm described in lecture.

Answer 3
--------

- [ ] In the best case, the number of compares to quicksort an array of N distinct keys is linear.
- [x] Suppose that quicksort is modified to use an explicit stack instead of recursion and to always recur on the subarray with fewer items before the subarray with more items. Then, the order of growth of the maximize size of the stack is log N in the worst case.
- [x] The expected number of compares to quicksort an array of N distinct keys depends only on the size of the array (and not the items in the array).
- [ ] The primary reason to use the first entry in the array as the partitioning item instead of the last entry is to guarantee performance (probabilistically).
- [ ] Median-of-3 partitioning is useful in practice but it does not reduce either the expected number of compares or exchanges.
