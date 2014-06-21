from UnionFind import WeightedQuickUnion

class UnionFindByHeight(WeightedQuickUnion):
    def __init__(self, N):
        super(UnionFindByHeight, self).__init__(N)


    def root(self, i):
        return super(UnionFindByHeight, self).root(i)

    def connected(self, p, q):
        return super(UnionFindByHeight, self).connected(p, q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
        else:
            self.id[j] = i

            if self.sz[i] == self.sz[j]:
                self.sz[i] += 1

    def find(self, i):
        return self.mx[self.root(i)]
