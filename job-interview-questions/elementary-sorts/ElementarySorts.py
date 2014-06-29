import random

def shuffleList(lst):
    n = len(lst)

    for i in range(n):
        rand = random.randint(0, i)
        lst[i], lst[rand] = lst[rand], lst[i]

    return lst

class SelectionSort:
    @staticmethod
    def sort(lst, comparable=(lambda x, y: 1 if (x < y) else (-1 if (x > y) else 0))):
        for x, i in enumerate(lst):
            low = x
            for y in range(x+1, len(lst)):
                if comparable(lst[y], lst[low]) > 0:
                    low = y

            lst[x], lst[low] = lst[low], lst[x]

        return lst

class InsertionSort:
    @staticmethod
    def sort(lst, comparable=(lambda x, y: 1 if (x < y) else (-1 if (x > y) else 0))):
        for x, i in enumerate(lst):
            for y in range(x, 0, -1):
                if comparable(lst[y], lst[y-1]) > 0:
                    lst[y], lst[y-1] = lst[y-1], lst[y]
                else:
                    break

        return lst

    @classmethod
    def _insert(cls, lst, i, comparable):
        if len(lst) == 0:
            return [i]
        elif comparable(i, lst[0]) > 0:
            return [i] + lst
        else:
            return [lst[0]] + cls._insert(lst[1:], i, comparable)

    @classmethod
    def recursive(cls, lst, comparable=(lambda x, y: 1 if (x < y) else (-1 if (x > y) else 0))):
        if len(lst) <= 1:
            return lst

        return cls._insert(cls.recursive(lst[1:], comparable), lst[0], comparable)

class ShellSort:
    @staticmethod
    def sort(lst, comparable=(lambda x, y: 1 if (x < y) else (-1 if (x > y) else 0))):
        n = len(lst)
        h = 1
        while h < n/3:
            h = 3*h + 1

        while h >= 1:
            for x in range(h, n):
                for y in range(x, h-1, -h):
                    if comparable(lst[y], lst[y-h]) > 0:
                        lst[y], lst[y-h] = lst[y-h], lst[y]
                    else:
                        break

            h /= 3

        return lst

print SelectionSort.sort(shuffleList([i for i in range(10)]))
print InsertionSort.sort(shuffleList([i for i in range(10)]))
print InsertionSort.recursive(shuffleList([i for i in range(10)]))
print ShellSort.sort(shuffleList([i for i in range(10)]))