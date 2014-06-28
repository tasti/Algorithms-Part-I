from StacksAndQueues import Stack

class QueueWithTwoStacks:
    def __init__(self):
        self.stackA = Stack()
        self.stackB = Stack()

    def enqueue(self, item):
        self.stackA.push(item)

    def popAToB(self):
        while not self.stackA.isEmpty():
            self.stackB.push(self.stackA.pop())

    def dequeue(self):
        if self.stackB.isEmpty():
            self.popAToB()

        return self.stackB.pop()

    def peek(self):
        if self.stackB.isEmpty():
            self.popAToB()

        return self.stackB.peek()

    def isEmpty(self):
        return self.stackA.isEmpty() and self.stackB.isEmpty()

    def size(self):
        return self.stackA.size() + self.stackB.size()

    def toList(self):
        lstB = self.stackB.toList()
        lstA = self.stackA.toList()
        lstB.reverse()
        print lstB, lstA
        return lstB + lstA
