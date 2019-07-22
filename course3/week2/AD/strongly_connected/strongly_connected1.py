#Uses python3

import sys
sys.setrecursionlimit(200000)


def DepthFirstSearchUpdateNodes(adj, startPoint, allNodes, nodeVals):
    if startPoint in allNodes:
        allNodes.discard(startPoint)
        neighborhoodlocal = set(x for x in adj[startPoint] if x in allNodes)
        while neighborhoodlocal:
            nextNode = neighborhoodlocal.pop()
            DepthFirstSearchUpdateNodes(adj, nextNode, allNodes, nodeVals)
            neighborhoodlocal = set(x for x in neighborhoodlocal if x in
                                    allNodes)
        #nodeVals.insert(0, startPoint)
        nodeVals.append(startPoint)

def DepthFirstSearch2(adj, startPoint, allNodes):
    neighborhoodlocal = set(x for x in adj[startPoint] if x in allNodes)
    allNodes.discard(startPoint)
    #print("startPoint=",startPoint, "neighborhoodlocal=", neighborhoodlocal)
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        #connected.add(nextNode)
        allNodes.discard(nextNode)
        DepthFirstSearch2(adj, nextNode, allNodes)


def number_of_strongly_connected_components(adj, adjb, n):
    if n == 2:
        return 1
    allNodes, nodeVals = set(range(n)), []
    while allNodes:
        startPoint = next(iter(allNodes))
        DepthFirstSearchUpdateNodes(adjb, startPoint, allNodes, nodeVals)

    allNodes, result, connected = set(range(n)), 0, []
    #print("nodeVals=", nodeVals)
    while nodeVals:
        connected.append(set())
        startPoint = nodeVals.pop()
        connected[result].add(startPoint)
        allNodes.remove(startPoint)
        DepthFirstSearch2(adj, startPoint, allNodes)
        #print("nodeVals",nodeVals)
        nodeVals = list(filter(lambda x: x in allNodes, nodeVals))
        result += 1
    #print(connected)
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
