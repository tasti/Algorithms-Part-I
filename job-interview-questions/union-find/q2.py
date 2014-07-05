import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../algorithms-and-data-structures'))

from UnionFind import WeightedQuickUnion

class UnionFindWithMax(WeightedQuickUnion):
    def __init__(self, N):
        super(UnionFindWithMax, self).__init__(N)

        self.mx = [i for i in range(N)]

    def root(self, i):
        return super(UnionFindWithMax, self).root(i)

    def connected(self, p, q):
        return super(UnionFindWithMax, self).connected(p, q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]

            self.mx[j] = max(self.mx[i], self.mx[j])
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

            self.mx[i] = max(self.mx[i], self.mx[j])

    def find(self, i):
        return self.mx[self.root(i)]
