import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../algorithms-and-data-structures'))

from StacksAndQueues import Node

def isCyclic(llist):
    slow = llist
    fast = llist

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow and fast and (slow == fast):
            return slow.item

    return False
