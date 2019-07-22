# python3
import sys
from functools import reduce

def build_tree(patterns):
    tree = dict()
    symbolIndex = 1
    for p in patterns:
        currentTree = tree.get(0, {})
        pLength=len(p)
        if p[0] not in currentTree:
            currentTree[p[0]] = symbolIndex
            symbolIndex += 1
            tree[0] = currentTree
        nextNode = currentTree[p[0]]
        for depth in range(1, pLength-1):
            currentTree = tree.get(nextNode, {})
            if p[depth] not in currentTree:
                currentTree[p[depth]] = symbolIndex
                symbolIndex += 1
                tree[nextNode] = currentTree
            nextNode = currentTree[p[depth]]
        currentTree = tree.get(nextNode, {})
        if p[pLength-1] not in currentTree:
            currentTree[p[pLength-1]] = symbolIndex
            symbolIndex += 1
            tree[nextNode] = currentTree
        tree[nextNode][-1]='x'
        # print("nextNode",nextNode)
        # print("tree[nextNode]",tree[nextNode])


    return tree

def onePass(newText, tree):
    pidx, nextNode = 0, 0
    if newText[pidx] not in tree[nextNode]: return False
    nextNode = tree[nextNode][newText[pidx]]
    textLength=len(newText)
    while pidx<textLength-1:
        pidx+=1
        nextNode = tree[nextNode].get(newText[pidx],-1)
        if nextNode == -1 or nextNode not in tree:
            return False
    print("tree[nextNode]",tree[nextNode],"nextNode",nextNode,-1 in tree[nextNode])
    if nextNode not in tree:
        return False
    else:
        return -1 in tree[nextNode]

def solve(text, patterns, L):
    result = []
    tree = build_tree(patterns)
    maxPatternLength = reduce(lambda x, y: max(x, y),
                              map(lambda x: len(x), patterns))
    minPatternLength = reduce(lambda x, y: min(x, y),
                              map(lambda x: len(x), patterns))
    for pos in range(L-maxPatternLength):
        if onePass(text[pos:pos+maxPatternLength], tree):
            result.append(pos)

    for pos in range(L-maxPatternLength,L-minPatternLength+1):
        if onePass(text[pos:], tree):
            result.append(pos)
    return result
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = set()
L = len(text)
for i in range(n):
    newPattern = sys.stdin.readline().strip()
    if len(newPattern)<=L and newPattern is not '':
        patterns.add(newPattern)
ans = solve(text, patterns, L)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
