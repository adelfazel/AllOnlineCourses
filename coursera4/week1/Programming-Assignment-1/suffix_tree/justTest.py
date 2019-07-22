def traverseTree(route, tree):
    treePointer = tree
    for r in route:
        treePointer = treePointer[r]
        print(treePointer)
        
        
def testtraverseTree():
    tree = {"a":1,"b":2,"c":{"a":2,"b":3, "d":{"a":3,"d":5}}}
    route1 = ["c","a"]
    route2 = ["c","d"]
    traverseTree(route1,tree)
    traverseTree(route2,tree)
    
    

def run():
    testtraverseTree()

def dictify(L):
    res = {}
    for e in L:
        res[e]=res.get(e,0)+1
    return res


def diffDict(d1,d2):
    for k in d1:
        if d1[k]!=d2[k]:
            print(f"k:{k} d1:{d1[k]} d2:{d2[k]}")
    for k in d2:
        if d1[k]!=d2[k]:
            print(f"k:{k} d1:{d1[k]} d2:{d2[k]}")
                  
                  
