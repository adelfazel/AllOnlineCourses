#Uses python3

import sys


def bipartite(adj):
    allNodes = set(range(n))
    if n < 2:
        return 0
    allNodeVals = [0]*n
    while allNodes:
        firstNode = allNodes.pop()
        queued = [firstNode]
        allNodeVals[firstNode] = 1
        while queued:
            st = queued.pop()
            allNodes.discard(st)
            currnetState = allNodeVals[st]
            neighbors = [x for x in adj[st]]
            bad = [x for x in neighbors if allNodeVals[x] == currnetState]
            if bad:
                return 0
            neighborsNew = [x for x in neighbors if allNodeVals[x] == 0]
            for ne in neighborsNew:
                allNodeVals[ne] = -currnetState
            queued.extend(neighborsNew)
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
