#Uses python3

import sys

def getNeighborhood(adj,point,reached):
    return [p for p in adj[point] if p not in reached]

Allneighborhood=[]
reached=[]

def breathFirstSearch(adj,start,finish):
    neighborhood=getNeighborhood(adj,start,reached)
    Allneighborhood.extend(neighborhood)
    reached.extend(neighborhood)
    if finish in Allneighborhood:
        return 1
    elif Allneighborhood== []:
        return 0
    else:
        newPoint=Allneighborhood.pop()
        return breathFirstSearch(adj,newPoint,finish)

def reach(adj,start,finish):
    if start==finish: return 1
    reached.append(start)
    return breathFirstSearch(adj,start,finish)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    nodesNum, edgeNum = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * edgeNum):2], data[1:(2 * edgeNum):2]))
    enterNode, exitNode = data[2 * edgeNum:]
    adj = [[] for _ in range(nodesNum)]
    enterNode, exitNode = enterNode - 1, exitNode - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, enterNode, exitNode))
