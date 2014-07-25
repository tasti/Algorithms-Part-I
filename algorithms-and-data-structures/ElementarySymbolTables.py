class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, comparator=(lambda x, y: 1 if (x > y) else (-1 if (x < y) else 0))):
        self.root = None
        self.comparator = comparator

    def _putHelper(self, key, value, node):
        if node == None:
            return Node(key, value)

        c = self.comparator(key, node.key)

        if c > 0:
            node.right = self._putHelper(key, value, node.right)
        elif c < 0:
            node.left = self._putHelper(key, value, node.left)
        else:
            node.value = value

        return node

    def put(self, key, value):
        self.root = self._putHelper(key, value, self.root)

    def get(self, key):
        node = self.root

        while node != None:
            c = self.comparator(key, node.key)

            if c > 0:
                node = node.right
            elif c < 0:
                node = node.left
            else:
                return node.value

        return None

    def _getRHelper(self, key, node):
        if node == None:
            return None

        c = self.comparator(key, node.key)

        if c > 0:
            return self._getRHelper(key, node.right)
        elif c < 0:
            return self._getRHelper(key, node.left)
        else:
            return node.value

    def getR(self, key):
        return self._getRHelper(key, self.root)

    def delete(self):
        pass
