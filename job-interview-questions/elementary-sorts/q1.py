from ElementarySorts import ShellSort

def less(p, q):
    if p[0] < q[0]:
        return 1
    elif p[0] > q[0]:
        return -1
    elif p[1] < q[1]:
        return 1
    elif p[1] > q[1]:
        return -1
    else:
        return 0

def intersection(a, b):
    a = ShellSort.sort(a, less)
    b = ShellSort.sort(b, less)
    i = 0
    j = 0
    aANDb = []

    while (i < len(a)) and (j < len(b)):
        compare = less(a[i], b[j])
        if compare > 0:
            i += 1
        elif compare < 0:
            j += 1
        else:
            aANDb.append(a[i])
            i += 1
            j += 1

    return aANDb
