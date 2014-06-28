Stacks and Queues
=================

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

(seed = 24632)
Suppose that an intermixed sequence of 10 push and 10 pop operations are performed
on a LIFO stack. The pushes push the letters 0 through 9 in order; the pops
print out the return value. Which of the following output sequence(s) could occur?
Check all that apply.

Answer 1
--------

- [ ] 2 4 1 6 7 5 9 8 3 0
- [x] 2 1 0 3 4 5 7 6 8 9
- [ ] 0 4 3 2 5 7 9 6 8 1
- [x] 6 5 4 3 2 1 0 7 8 9
- [x] 0 3 2 4 5 1 6 9 8 7

Question 2
----------

(seed = 50828)
Suppose that an intermixed sequence of 10 enqueue and 10 dequeue operations are performed
on a FIFO queue. The enqueues add the letters 0 through 9 in order; the dequeues
print out the return value. Which of the following output sequence(s) could occur?
Check all that apply.


Answer 2
--------

- [ ] 0 1 2 3 4 5 6 9 8 7
- [ ] 0 1 2 3 4 5 7 9 6 8
- [ ] 0 3 5 2 6 1 8 9 4 7
- [ ] 0 1 2 3 4 8 6 9 5 7
- [x] 0 1 2 3 4 5 6 7 8 9

Question 3
----------

(seed = 525707)
Consider an object of type MysteryBox that stores N items of type double
in a doubly-linked list of N nodes, referenced by first.

    public class MysteryBox {
        private Node first;

        private static class Node {
            private double item;
            private Node next;
            private Node prev;
        }

        ...
    }


Using the 64-bit memory cost model from the lecture, how many bytes does it use as a function of N?
Include all memory referenced by the object and use tilde notation to simplify your answer.
For example, enter ~ 4N if the number of bytes as a function of N is 4N + 32.

Note that an object from a static nested class does not store a reference to the
instance of its enclosing class, so there is no 8-byte inner class overhead here.

Answer 3
--------

Object overhead (MysteryBox): 16
first: 8

Object overhead (Node): 16
item: 8
next: 8
prev: 8

Total: 24 + 40N

~ 40N
