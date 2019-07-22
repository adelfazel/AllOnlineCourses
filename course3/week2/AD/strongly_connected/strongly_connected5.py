#Uses python3

import sys
sys.setrecursionlimit(200000)


def DepthFirstSearchUpdateNodes(adj, adjb, startPoint, allNodes, nodeVals):
    allNodes.discard(startPoint)
    for n in adjb[startPoint]:
        adj[n].discard(startPoint)
    neighborhoodlocal = adj[startPoint]
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        allNodes.discard(nextNode)
        for n in adjb[nextNode]:
            adj[n].discard(nextNode)
        DepthFirstSearchUpdateNodes(adj, adjb, nextNode, allNodes, nodeVals)
        #neighborhoodlocal = set(x for x in neighborhoodlocal if x in allNodes)

    nodeVals.append(startPoint)


def DepthFirstSearch2(adj, adjb, startPoint, explored):

    for n in adjb[startPoint]:
        adj[n].discard(startPoint)
    #allNodes.discard(startPoint)
    neighborhoodlocal = adj[startPoint]
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        explored.add(nextNode)
        for n in adjb[nextNode]:
            adj[n].discard(nextNode)
        #allNodes.discard(nextNode)
        DepthFirstSearch2(adj, adjb, nextNode, explored)
    return explored

def number_of_strongly_connected_components(adj, adjb, n):
    if n == 2:
        return 1
    allNodes, nodeOrders = set(range(n)), []
    adjb_back = adjb.copy()
    while allNodes:
        st = allNodes.pop()
        DepthFirstSearchUpdateNodes(adjb_back, adj, st, allNodes, nodeOrders)

    allNodes, result = set(range(n)), 0
    while nodeOrders:
        startPoint = nodeOrders.pop()
        explored = DepthFirstSearch2(adj, adjb, startPoint, set([startPoint]))
        nodeOrders = [x for x in nodeOrders if x not in explored]
        result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [set() for _ in range(n)]
    adjb = [set() for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].add(b - 1)
        adjb[b-1].add(a-1)

    print(number_of_strongly_connected_components(adj, adjb, n))
