#Uses python3

import sys
sys.setrecursionlimit(200000)


def DepthFirstSearchUpdateNodes(adj, startPoint, nodeVals, explored):
    neighborhoodlocal = set(x for x in adj[startPoint] if x not in explored)
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        explored.add(nextNode)
        DepthFirstSearchUpdateNodes(adj, nextNode, nodeVals, explored)
        neighborhoodlocal = set(x for x in neighborhoodlocal if x not in explored)
    nodeVals.append(startPoint)


def DepthFirstSearch(adj, startPoint, explored):
    neighborhoodlocal = set(x for x in adj[startPoint] if x not in explored)
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        explored.add(nextNode)
        DepthFirstSearch(adj, nextNode, explored)
        neighborhoodlocal.difference_update(explored)


def bellman_ford(adj,  distance, cost, changed, reachable):
    for s in reachable:
        costs = cost[s]
        edges = adj[s]
        nodeDistance = distance[s]
        for edgeIndex in range(len(edges)):
            if distance[edges[edgeIndex]] > nodeDistance+costs[edgeIndex]:
                changed.add(edges[edgeIndex])
                distance[edges[edgeIndex]] = nodeDistance+costs[edgeIndex]


def shortet_paths(adj, adjb, cost, s, distance, reachable, shortest, n):
    distance[s] = 0
    reachableFromSt = set()
    DepthFirstSearch(adj, s, reachableFromSt)
    reachableFromSt.add(s)
    for _ in range(n-1):
        bellman_ford(adj, distance, cost, set(),  reachableFromSt)
    changedNodes = set()
    for _ in range(n+2):
        bellman_ford(adj, distance, cost, changedNodes, reachableFromSt)

    for node in range(n):
        if node not in reachableFromSt:
            reachable[node] = 1
    for c in changedNodes:
        shortest[c] = 1
    if changedNodes:
        nodeVals, explored = [], set()
        while reachableFromSt:
            startPoint = reachableFromSt.pop()
            explored.add(startPoint)
            DepthFirstSearchUpdateNodes(adjb, startPoint, nodeVals, explored)
            reachableFromSt.difference_update(explored)
        explored, connected, exploredSoFar = set(), [], set()
        while nodeVals:
            startPoint = nodeVals.pop()
            explored.add(startPoint)
            DepthFirstSearch(adj, startPoint, explored)
            connected.append(explored.difference(exploredSoFar))
            exploredSoFar.update(explored)
            for x in explored:
                if x in nodeVals:
                    nodeVals.remove(x)
            explored = set()
        for connectedPlace in connected:
            if changedNodes.intersection(connectedPlace):
                for c in connectedPlace:
                    shortest[c] = 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    adjb = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        adjb[b - 1].append(a - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [0] * n
    shortet_paths(adj, adjb, cost, s, distance, reachable, shortest, n)
    for x in range(n):
        if reachable[x] == 1:
            print('*')
        elif shortest[x] == 1:
            print('-')
        else:
            print(distance[x])
