Mergesort
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

(seed = 269457)
Give the array that results immediately after the 7th call to merge()
when top-down mergesorting the following array of size 12:

84 39 70 27 50 28 49 25 58 55 76 71

Answer 1
--------

27 28 39 50 70 84 25 49 58 55 76 71

Question 2
----------

(seed = 741548)
The column on the left contains the original input of 12 strings to be sorted;
the column on the right contains the strings in sorted order; the other 4 columns contain the
contents at some intermediate step during one of the 2 mergesorting algorithms listed below.

    rust   bark   bark   bark   bark   bark   
    bark   mint   buff   buff   buff   buff   
    mint   rust   mint   iris   mint   cafe   
    buff   buff   rust   mint   rust   herb   
    iris   iris   cafe   rust   cafe   iris   
    sand   sand   herb   sand   herb   jade   
    cafe   cafe   iris   cafe   iris   kobi   
    herb   herb   sand   herb   sand   mint   
    palm   palm   jade   palm   kobi   palm   
    kobi   kobi   kobi   jade   palm   pear   
    pear   pear   palm   kobi   jade   rust   
    jade   jade   pear   pear   pear   sand   
    ----   ----   ----   ----   ----   ----   
     0      ?      ?      ?      ?      3     


Match up each column with the corresponding mergesorting algorithm from the given list:

    0. Original input
    1. Top-down Mergesort (standard recursive version)
    2. Bottom-up Mergesort (nonrecursive version)
    3. Sorted

You may use an algorithm more than once. Your answer should be a sequence of 6 integers between
0 and 3 (starting with 0 and ending with 3) and with each integer separated by whitespace.

Hint: think about algorithm invariants. Do not trace code.

Answer 2
--------

0 1 2 1 2 3

Question 3
----------

(seed = 261123)
Which of the following statements about mergesort are true? Check all that apply. Unless otherwise specified, assume that mergesort refers to the pure recursive (top-down) version of mergesort (with no optimizations), using the merging subroutine described in lecture.

Answer 3
--------

- [ ] Bottom-up mergesort uses only a constant amount of space (other than the input array).
- [x] Any compare-based sorting algorithm requires at least lg (N!) compares (in the worst case) to sort an array of N items.
- [ ] A single key can be involved in no more than ~ 1/2 N compares when mergesorting an array containing N distinct keys.
- [x] The number of recursive calls to sort() when mergesorting an array of N items (when N is a power of 2) is no more than 2N.
- [ ] Mergesort uses only a logarithmic amount of space (other than the input array).
