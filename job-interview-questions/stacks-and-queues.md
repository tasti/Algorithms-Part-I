Interview Questions: Stacks and Queues
======================================

Question 1
----------

**Queue with two stacks.** Implement a queue with two stacks so that each queue operations takes a constant amortized number of stack operations.

Answer 1
--------

Solution: stacks-and-queues/q1.py

Question 2
----------

**Stack with max.** Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation. Assume the elements are reals numbers so that you can compare them.

Answer 2
--------

Solution: stacks-and-queues/q2.py

Question 3
----------

**Java generics.** Explain why Java prohibits generic array creation.

Answer 3
--------

...

Question 4
----------

**Detect cycle in a linked list.** A singly-linked data structure is a data structure made up of nodes where each node has a pointer to the next node (or a pointer to null). Suppose that you have a pointer to the first node of a singly-linked list data structure:
- Determine whether a singly-linked data structure contains a cycle. You may use only two pointers into the list (and no other variables). The running time of your algorithm should be linear in the number of nodes in the data structure.
- If a singly-linked data structure contains a cycle, determine the first node that participates in the cycle. you may use only a constant number of pointers into the list (and no other variables). The running time of your algorithm should be linear in the number of nodes in the data structure.
You may not modify the structure of the linked list.

Answer 4
--------

Solution: stacks-and-queues/q4.py

Question 5
----------

**Clone a linked structure with two pointers per node.** Suppose that you are given a reference to the first node of a linked structure where each node has two pointers: one pointer to the next node in the sequence (as in a standard singly-linked list) and one pointer to an arbitrary node.
```
private class Node {
    private String item;
    private Node next;
    private Node random;
}
```
Design a linear-time algorithm to create a copy of the doubly-linked structure. You may modify the original linked structure, but you must end up with two copies of the original.

Answer 5
-------

...
