#python3
import sys


def fit_new_branch(text, tree, st, L):
    if text[st] == "$":
        tree["$"] = st
        return
    charPos = st
    treePointer = tree
    while text[charPos] in treePointer and charPos < L:
        treePointer = treePointer[text[charPos]]
        charPos += 1
    if text[charPos] == "$":
        treePointer["$"] = st
        return
    newTree = {}
    treePointer[text[charPos]] = newTree  # update last branch to a new branch
    treePointer = newTree  # Update the tree pointer to head of that branch
    charPos += 1
    if text[charPos] == "$":
        treePointer["$"] = st
        return
    while text[charPos] != "$":
        treePointer[text[charPos]] = {text[charPos+1]: st}
        treePointer = treePointer[text[charPos]]
        charPos += 1


def compactTree(tree):
    keys = tree.keys()
    for key in keys:
        if key == "$":
            return
        branchToMerge = tree[key]
        compactTree(branchToMerge)
        if len(branchToMerge) == 1:
            mergeKey = list(branchToMerge.keys())[0]
            newKey = key+mergeKey
            print(f"1:{tree}")
            print(f"2:{branchToMerge}")
            #print(f"newKey:{newKey} mergeKey:{mergeKey}")
            tree[newKey] = branchToMerge[mergeKey]
            del branchToMerge[mergeKey]
            return True
    return False

#def merge(tree,branchToMerge):


"""
def compactTree(tree):
    branches = tree.keys()
    for branch in branches:
        if "$" not in branch:
            branchToMerge = tree[branch]
            if len(branchToMerge) == 1:

"""


def build_suffix_tree(text):
    tree = {}
    L = len(text)
    for text_start_point in range(L):
        # check if newrecord has a substring that matches exisitng records
        fit_new_branch(text, tree, text_start_point, L)
        #print(f"tree:{tree}")
    while compactTree(tree):
        pass

    return tree


def printReslt(tree):
    for branch in tree:
        print(branch)
        if "$" not in branch:
            printReslt(tree[branch])


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    printReslt(result)
