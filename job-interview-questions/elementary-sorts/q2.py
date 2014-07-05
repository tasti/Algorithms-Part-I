import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../algorithms-and-data-structures'))

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
