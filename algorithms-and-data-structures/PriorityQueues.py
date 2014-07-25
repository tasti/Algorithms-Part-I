from ElementarySorts import shuffleList

class BinaryHeap:
    # Default to max-heap. For min-heap,
    # set comparator=(lambda x, y: 1 if (x < y) else (-1 if (x > y) else 0))
    def __init__(self, lst=[], comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        self.pq = [None] + lst
        self.comparator = comparator

    def swap(self, a, b):
        self.pq[a], self.pq[b] = self.pq[b], self.pq[a]

    def _swim(self, k):
        while k > 1 and self.comparator(self.pq[k/2], self.pq[k]) < 0:
            self.swap(k, k/2)
            k /= 2

    def insert(self, item):
        self.pq.append(item)
        self._swim(self.size())

    def _sink(self, k, N=None):
        N = self.size() if N == None else N

        while 2*k <= N:
            j = 2*k

            if j < N and self.comparator(self.pq[j], self.pq[j+1]) < 0:
                j += 1
            if not self.comparator(self.pq[k], self.pq[j]) < 0:
                break

            self.swap(k, j)
            k = j

    # Deletes the item with the highest priority
    def delete(self):
        if self.isEmpty():
            return None

        mx = self.max()
        self.swap(1, self.size())
        self.pq.pop()
        self._sink(1)

        return mx

    def max(self):
        if self.isEmpty():
            return None

        return self.pq[1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.pq) - 1

    def toList(self):
        return self.pq[1:]

class HeapSort:
    @staticmethod
    def sort(lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        N = len(lst)
        pq = BinaryHeap(lst, comparator)

        for k in range(N/2, 0, -1):
            pq._sink(k)

        while (N > 1):
            pq.swap(1, N)
            N -= 1
            pq._sink(1, N)

        return pq.toList()
