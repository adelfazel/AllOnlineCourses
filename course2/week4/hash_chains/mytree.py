class node:
    def __init__(self, parent=None, right=None, left=None, key):
        self._parent = parent
        self._right = right
        self._left = left
        self._height = 1
        self.key = key

    def getParent(self):
        return self._parent

    def getRight(self):
        return self._right

    def getLeft(self):
        return self._left


class myTree:

    def __init__(self):
        self.node = None

    def insert(self, elem):
        pass

    def find(self, elem):
        if self.node.getLeft() is not None:
            if self.node.getLeft()

    def next(self, elem):
        pass
