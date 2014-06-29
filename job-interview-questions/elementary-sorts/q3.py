def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def color(lst, i):
    return lst[i]

def sortDNF(lst):
    x = 0
    i = 0
    j = len(lst) - 1

    while x <= j:
        c = color(lst, x)

        if c == 'r':
            swap(lst, x, i)
            i += 1
            x += 1
        elif c == 'b':
            swap(lst, x, j)
            j -= 1
        else:
            x += 1

    return lst
