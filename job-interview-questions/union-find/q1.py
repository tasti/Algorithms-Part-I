import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../algorithms-and-data-structures'))

from UnionFind import WeightedQuickUnion

class UnionFindWithCount(WeightedQuickUnion):
    def __init__(self, N):
        super(UnionFindWithCount, self).__init__(N)

        self.groups = N

    def root(self, i):
        return super(UnionFindWithCount, self).root(i)

    def connected(self, p, q):
        return super(UnionFindWithCount, self).connected(p, q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.groups -= 1

    def count(self):
        return self.groups

r = file('q1.in', 'r')
w = file('q1.out', 'w')

C = int(r.readline())

for c in range(C):
    N = int(r.readline())
    M = int(r.readline())

    socialNetwork = UnionFindWithCount(N)
    done = False

    for m in range(M):
        line = map(int, r.readline().split())
        A = line[0]
        B = line[1]
        T = line[2]

        socialNetwork.union(A, B)

        if socialNetwork.count() == 1:
            w.write('%d\n' % T)
            done = True
            break
    
    if not done:
        w.write('Never\n')
