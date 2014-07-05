class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.first = None
        self.sz = 0

    def push(self, item):
        old = self.first
        self.first = Node(item, old)
        self.sz +=1

    def pop(self):
        if self.isEmpty():
            return None

        popped = self.first.item
        self.first = self.first.next
        self.sz -=1

        return popped

    def peek(self):
        if self.isEmpty():
            return None

        return self.first.item

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.sz

    def toList(self):
        lst = []
        current = self.first

        while current:
            lst.append(current.item)
            current = current.next

        lst.reverse()
        return lst

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.sz = 0

    def enqueue(self, item):
        oldLast = self.last
        self.last = Node(item, None)
        
        if self.isEmpty():
            self.first = self.last
        else:
            oldLast.next = self.last

        self.sz += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        dequeued = self.first.item
        self.first = self.first.next
        self.sz -= 1

        if self.isEmpty():
            self.last = None

        return dequeued

    def peek(self):
        if self.isEmpty():
            return None

        return self.first.item

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.sz

    def toList(self):
        lst = []
        current = self.first

        while current:
            lst.append(current.item)
            current = current.next

        return lst
