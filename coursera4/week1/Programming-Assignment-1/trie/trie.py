#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    symbolIndex = 1
    for p in patterns:
        currentTree = tree.get(0, {})
        if p[0] not in currentTree:
            currentTree[p[0]] = symbolIndex
            symbolIndex += 1
            tree[0] = currentTree
        nextNode = currentTree[p[0]]
        for depth in range(1, len(p)):
            currentTree = tree.get(nextNode, {})
            if p[depth] not in currentTree:
                currentTree[p[depth]] = symbolIndex
                symbolIndex += 1
                tree[nextNode] = currentTree
            nextNode = currentTree[p[depth]]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
