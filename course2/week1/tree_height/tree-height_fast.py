# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.children=[set() for _ in range(self.n)]
        self.root=None
        self.group_children()
    def group_children(self):
        for idx,child in enumerate(self.parent):
            if child==-1:
                self.root=idx
            else:
                self.children[child].add(idx)

    def compute_height(self):
        heights=set()
        for child in self.children[self.root]:
            #print("child:%d"%child)
            heights.add(self.recurssive_compute_height(child,1))
        return max(heights)
    def recurssive_compute_height(self,parent,current_height):
        if not bool(self.children[parent]):
            return current_height+1
        heights=set()
        for child in self.children[parent]:
            #print("grand_child:%d,height%d"%(child,current_height+1))
            heights.add(self.recurssive_compute_height(child,current_height+1))
        return max(heights)


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
