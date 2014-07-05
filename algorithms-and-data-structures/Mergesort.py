from ElementarySorts import shuffleList

class MergeSort:
    @classmethod
    def sort(cls, lst, comparable=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        return cls._sortHelper(lst, [], 0, len(lst) - 1, comparable)

    @classmethod
    def bottomUp(cls, lst, comparable=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        n = len(lst)
        aux = []
        sz = 1

        for i in xrange(1, n, sz):
            for lo in xrange(0, n-sz, sz+sz):
                cls._merge(lst, aux, lo, lo+sz-1, min(lo+sz+sz-1, n-1), comparable)

            sz *= 2

        return lst


    @classmethod
    def _sortHelper(cls, lst, aux, lo, hi, comparable):
        if lo < hi:
            mid = (hi+lo) / 2

            cls._sortHelper(lst, aux, lo, mid, comparable)
            cls._sortHelper(lst, aux, mid+1, hi, comparable)

            if comparable(lst[mid], lst[mid+1]) > 0:
                cls._merge(lst, aux, lo, mid, hi, comparable)

        return lst

    @classmethod
    def _merge(cls, lst, aux, lo, mid, hi, comparable):
        aux = lst[:]
        i = lo
        j = mid + 1

        for k in xrange(lo, hi+1):
            if i > mid:
                lst[k] = aux[j]
                j += 1
            elif j > hi:
                lst[k] = aux[i]
                i += 1
            elif comparable(aux[j], aux[i]) < 0:
                lst[k] = aux[j]
                j += 1
            else:
                lst[k] = aux[i]
                i += 1

print MergeSort.bottomUp(shuffleList([i for i in range(10)]))