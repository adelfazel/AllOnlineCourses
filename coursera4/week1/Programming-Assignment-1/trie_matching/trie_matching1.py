# python3
import sys
from functools import reduce


def build_tree(patterns):
    tree = dict()
    tree[0] = {}
    ends = set()
    symbolIndex = 1
    for p in patterns:
        currentTree = tree[0]
        pLength = len(p)
        newChar = p[0]
        if newChar not in currentTree:
            currentTree[newChar] = symbolIndex
            symbolIndex += 1
            tree[0] = currentTree
        nextNode = currentTree[newChar]
        if pLength == 1:
            ends.add(nextNode)
            continue
        for depth in range(1, pLength):
            currentTree = tree.get(nextNode, {})
            newChar = p[depth]
            if newChar not in currentTree:
                currentTree[newChar] = symbolIndex
                symbolIndex += 1
                tree[nextNode] = currentTree
            nextNode = currentTree[newChar]
        ends.add(nextNode)
    return (tree, ends)


def onePass(newText, tree, ends, textLength):
    pidx, newBranch, newChar = 0, tree[0], newText[0]
    #print(newText)
    if newChar not in newBranch:
        return False
    nextNode = newBranch[newChar]
    if nextNode in ends:
        return True
    while nextNode in tree and pidx < textLength:

        pidx += 1
        newChar = newText[pidx]
        #print("newChar=","pidx=",pidx)
        newBranch = tree[nextNode]
        if newChar in newBranch:
            nextNode = newBranch[newChar]
            if nextNode in ends:
                return True

        else:
            return False

    return False


def solve(text, patterns, L):
    result = []
    (tree, ends) = build_tree(patterns)
    #print(tree, ends)
    maxPatternLength = reduce(lambda x, y: max(x, y),
                              map(lambda x: len(x), patterns))
    minPatternLength = reduce(lambda x, y: min(x, y),
                              map(lambda x: len(x), patterns))
    for pos in range(L-maxPatternLength):
        if onePass(text[pos:pos+maxPatternLength],
                   tree, ends, maxPatternLength):
            result.append(pos)
    for pos in range(L-maxPatternLength, L-minPatternLength+1):
        if onePass(text[pos:], tree, ends, len(text[pos:])-1):
            result.append(pos)
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = set()
L = len(text)
for i in range(n):
    newPattern = sys.stdin.readline().strip()
    if len(newPattern) <= L and newPattern is not '':
        patterns.add(newPattern)
ans = solve(text, patterns, L)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
