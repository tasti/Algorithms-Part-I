Analysis of Algorithms
======================

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

(seed = 64956)
Suppose that you time a program as a function of N and produce
the following table.

        N   seconds
-------------------
     2048     0.000
     4096     0.000
     8192     0.001
    16384     0.004
    32768     0.013
    65536     0.038
   131072     0.114
   262144     0.342
   524288     1.023
  1048576     3.069
  2097152     9.199
  4194304    27.551
  8388608    82.544
 16777216   247.389
 33554432   741.399
 67108864  2221.173


Estimate the order of growth of the running time as a function of N.
Assume that the running time obeys a power law T(N) ~ a N^b. For your
answer, enter the constant b. Your answer will be marked as correct
if it is within 1% of the target answer - we recommend using
two digits after the decimal separator, e.g., 2.34.

Answer 1
--------

log<sub>2</sub>(2221.173 / 741.399)

1.58

Question 2
----------

(seed = 438760)
What is the order of growth of the worst case running time of the following code fragment
as a function of N?

int sum = 0;
for (int i = 1; i <= N; i++)
    for (int j = 1; j <= i*i*i; j++)
        sum++;

Answer 2
--------


- [ ] 1
- [ ] log N
- [ ] N^(1/2)
- [ ] N
- [ ] N log N
- [ ] N^(3/2)
- [ ] N^2
- [ ] N^2 log N
- [ ] N^(5/2)
- [ ] N^3
- [x] N^4
- [ ] N^5
- [ ] N^6
- [ ] N^7

Question 3
----------

(seed = 51036)
Given the following definition of a MysteryBox object: 

public class MysteryBox {
    private int x0, x1;
    private boolean y0, y1;
    private long z0, z1, z2;
    private double[] a = new double[320];

    ...
}


Using the 64-bit memory cost model from lecture, how many bytes does each object of type MysteryBox use?

Answer 3
--------

Object overhead: 16
x0: 4
x1: 4
y0: 1
y1: 1
z0: 8
z1: 8
z2: 8
a: 8*320 + 24
Reference: 8
Padding: 6

2648
