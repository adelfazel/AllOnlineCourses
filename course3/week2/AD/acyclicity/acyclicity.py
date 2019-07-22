#Uses python3
import sys

def getAllNodes(adj):
    allNodes = set()
    for node in adj:
        for node_next in node:
            if node_next not in allNodes:
                allNodes.add(node_next)
    return allNodes


def DepthFirstSearch(adj, activePath):
    neighborhood = adj[activePath[-1]]
    if neighborhood:
        for n in neighborhood:
            if n in activePath:
                return 1

        for n in neighborhood:
            newPath = activePath.copy()
            newPath.append(n)
            if DepthFirstSearch(adj, newPath) == 1:
                return 1
    return set(activePath)


def acyclic(adj):
    if len(adj) < 2:
        return 0
    allConnectedNodes = getAllNodes(adj)
    while allConnectedNodes:
        startPoint = allConnectedNodes.pop()
        connectedPoints = DepthFirstSearch(adj, [startPoint])
        if connectedPoints == 1:
            return 1
        else:
            allConnectedNodes.difference_update(connectedPoints)
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
