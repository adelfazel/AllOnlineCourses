# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
class Node:
    def __init__(self,children):
        self.children=[]

class TreeHeight:
        def createTree(self):
            self.tree=[0]*(self.n-1)
            for elemIndex in range(self.n):
                 self.tree[elemIndex]=[i for i, x in enumerate(self.parent) if x == self.parent[elemIndex]]
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
            createTree()
            # self.n=5
            # self.parent = list(map(int, "-1 0 4 0 3".split()))

        def find_root(self):
            return self.parent.index(-1)
        def find_children(self,elem):
            return [i for i, x in enumerate(self.parent) if x == elem]
        def compute_height(self):
            root = self.find_root()
            allChildren=self.find_children(root)
            heights = list(map(lambda x:self.recurssive_compute_height(2,x),allChildren))
            if len(heights)>1:
                return max(heights)
            else: return heights[0]
        def recurssive_compute_height(self,currentDepth,parent):
            allChildren=self.find_children(parent)
            if not allChildren:
                return currentDepth
            heights = list(map(lambda x:self.recurssive_compute_height(currentDepth+1,x),allChildren))
            if len(heights)>1:
                return max(heights)
            else: return heights[0]

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
