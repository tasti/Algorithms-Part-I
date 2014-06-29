from ElementarySorts import ShellSort

def isPermutation(a, b):
    if len(a) != len(b):
        return False

    a = ShellSort.sort(a)
    b = ShellSort.sort(b)

    for i, j in zip(a, b):
        if i != j:
            return False

    return True
