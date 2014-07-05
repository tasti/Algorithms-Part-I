import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../algorithms-and-data-structures'))

from StacksAndQueues import Stack

class StackWithMax():
    def __init__(self):
        self.stack = Stack()
        self.mx = Stack()

    def max(self):
        return self.mx.peek()

    def push(self, item):
        if item >= self.max():
            self.mx.push(item)

        self.stack.push(item)

    def pop(self):
        popped = self.stack.pop()

        if popped == self.max():
            self.mx.pop()

        return popped

    def peek(self):
        return self.stack.peek()

    def isEmpty(self):
        return self.stack.isEmpty()

    def size(self):
        return self.stack.size()

    def toList(self):
        return self.stack.toList()
