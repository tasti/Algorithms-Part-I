class MergeSort:
    @classmethod
    def sort(cls, lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        return cls._sortHelper(lst, [], 0, len(lst) - 1, comparator)

    @classmethod
    def bottomUp(cls, lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        n = len(lst)
        aux = []
        sz = 1

        for i in xrange(1, n, sz):
            for lo in xrange(0, n-sz, sz+sz):
                cls._merge(lst, aux, lo, lo+sz-1, min(lo+sz+sz-1, n-1), comparator)

            sz *= 2

        return lst


    @classmethod
    def _sortHelper(cls, lst, aux, lo, hi, comparator):
        if lo < hi:
            mid = (hi+lo) / 2

            cls._sortHelper(lst, aux, lo, mid, comparator)
            cls._sortHelper(lst, aux, mid+1, hi, comparator)

            if comparator(lst[mid], lst[mid+1]) > 0:
                cls._merge(lst, aux, lo, mid, hi, comparator)

        return lst

    @classmethod
    def _merge(cls, lst, aux, lo, mid, hi, comparator):
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
            elif comparator(aux[j], aux[i]) < 0:
                lst[k] = aux[j]
                j += 1
            else:
                lst[k] = aux[i]
                i += 1
