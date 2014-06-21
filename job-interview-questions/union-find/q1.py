import UnionFind

r = file('q1.in', 'r')
w = file('q1.out', 'w')

C = int(r.readline())

for c in range(C):
    N = int(r.readline())
    M = int(r.readline())

    socialNetwork = UnionFind.WeightedQuickUnion(N)
    done = False

    for m in range(M):
        line = map(int, r.readline().split())
        A = line[0]
        B = line[1]
        T = line[2]

        socialNetwork.union(A, B)

        if max(socialNetwork.sz) == N:
            w.write('%d\n' % T)
            done = True
            break
    
    if not done:
        w.write('Never\n')