from ElementarySorts import shuffleList

class QuickSort:
    @classmethod
    def sort(cls, lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        lst = shuffleList(lst) # Guarantee performance
        
        return cls._sortHelper(lst, 0, len(lst) - 1, comparator)

    @classmethod
    def oneLiner(cls, lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        return lst if len(lst) <= 1 else cls.oneLiner([i for i in lst[1:] if i < lst[0]], comparator) + [lst[0]] + cls.oneLiner([i for i in lst[1:] if i >= lst[0]], comparator)

    @classmethod
    def _sortHelper(cls, lst, lo, hi, comparator):
        if hi <= lo:
            return

        j = cls._partition(lst, lo, hi, comparator)
        cls._sortHelper(lst, lo, j - 1, comparator)
        cls._sortHelper(lst, j + 1, hi, comparator)

        return lst

    @classmethod
    def _partition(cls, lst, lo, hi, comparator):
        pivot = lst[lo]
        pos = hi

        for i in range(hi, lo-1, -1):
            if comparator(lst[i], pivot) >= 0:
                lst[i], lst[pos] = lst[pos], lst[i]
                pos -= 1

        return pos+1

class QuickSelect:
    @classmethod
    def select(cls, lst, k, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        lst = shuffleList(lst) # Guarantee performance
        lo = 0
        hi = len(lst) - 1
        
        while (hi > lo):
            j = QuickSort._partition(lst, lo, hi, comparator)

            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                return lst[k]

        return lst[k]

class QuickSort3WayPartition:
    @classmethod
    def sort(cls, lst, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        lst = shuffleList(lst) # Guarantee performance
        
        return cls._sortHelper(lst, 0, len(lst) - 1, comparator)

    @classmethod
    def _sortHelper(cls, lst, lo, hi, comparator):
        if hi <= lo:
            return

        lt, gt = cls._partition(lst, lo, hi, comparator)
        cls._sortHelper(lst, lo, lt - 1, comparator)
        cls._sortHelper(lst, gt + 1, hi, comparator)

        return lst

    @classmethod
    def _partition(cls, lst, lt, gt, comparator):
        i = lt

        while (i <= gt):
            c = comparator(lst[i], lst[lt])

            if c < 0:
                lst[i], lst[lt] = lst[lt], lst[i]
                i += 1
                lt += 1
            elif c > 0:
                lst[i], lst[gt] = lst[gt], lst[i]
                gt -= 1
            else:
                i += 1

        return lt, gt
