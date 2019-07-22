#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def recursiveIsBST(tree, idx):
    #print("tree[idx][0]:", tree[idx][0], "tree[idx][1]:", tree[idx][1], "tree[idx][2]:", tree[idx][2])
    nodeVal = tree[idx][0]
    leftIdx = tree[idx][1]
    rightIdx = tree[idx][2]
    #print("idx:",idx,"nodeVal:",nodeVal,"L:",tree[idx][1],"R:",tree[idx][2])
    mn1,mx1,mn2,mx2=nodeVal,nodeVal,nodeVal,nodeVal
    if leftIdx == -1 and rightIdx == -1:
        return (nodeVal, nodeVal, True)

    if rightIdx != -1:
        (mn1, mx1, isGood) = recursiveIsBST(tree, rightIdx)
        if isGood is False or nodeVal > mn1:
            return (-1, -1, False)

    if leftIdx != -1:
        (mn2, mx2, isGood) = recursiveIsBST(tree, leftIdx)
        if isGood is False or nodeVal < mx2:
            return (-1, -1, False)
    return (min(mn1,mn2), max(mx1,mx2), True)


def IsBinarySearchTree(tree):
    if len(tree) < 2:
        return True
    return recursiveIsBST(tree, 0)[2]


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
        #print("tree:", tree)
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
