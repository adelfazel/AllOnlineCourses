# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(tableIdx):
    children=[]
    root = tableIdx
    while root!=parent[root]:
        children.append(root)
        root=parent[root]
    for child in children:
        parent[child]=root
    return root

    
def merge(destination, source):
    realDestination, realSource = getParent(destination),getParent(source)
    if realDestination == realSource:
        return False
    global ans
    if rank[realDestination]>rank[realSource]:
        parent[realSource]=parent[realDestination]
        lines[realDestination]+=lines[realSource]
        rank[realSource]=0
        lines[realSource]=0
        ans= max(ans,lines[realDestination])
    else:
        parent[realDestination]=parent[realSource]
        lines[realSource]+=lines[realDestination]
        rank[realDestination]=0
        lines[realDestination]=0
        if rank[realDestination]==rank[realSource]:
            rank[realSource]+=1
        ans= max(ans,lines[realSource])

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
