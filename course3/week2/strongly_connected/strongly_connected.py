#Uses python3

import sys
import heapq
sys.setrecursionlimit(200000)


def DepthFirstSearchUpdateNodes(adj, startPoint, allNodes, nodeVals):
    global counter
    if startPoint in allNodes:
        neighborhoodlocal = set(x for x in adj[startPoint] if x in allNodes)
        counter += 1
        #heapq.heappush(nodeVals, (counter, startPoint))
        allNodes.discard(startPoint)
        while neighborhoodlocal:
            nextNode = neighborhoodlocal.pop()
            DepthFirstSearchUpdateNodes(adj, nextNode, allNodes, nodeVals)
        counter += 1
        heapq.heappush(nodeVals, (counter, startPoint))


def DepthFirstSearch2(adj, startPoint, allNodes, res):
    neighborhoodlocal = set(x for x in adj[startPoint] if x in allNodes)
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        allNodes.discard(nextNode)
        res.add(nextNode)
        DepthFirstSearch2(adj, nextNode, allNodes, res)

def number_of_strongly_connected_components(adj, adjb, n):
    global counter
    counter = 0
    if n == 2:
        return 1
    allNodes, nodeVals = set(range(n)), []
    while allNodes:
        startPoint = next(iter(allNodes))
        DepthFirstSearchUpdateNodes(adj, startPoint, allNodes, nodeVals)

    allNodes, result, res = set(range(n)), 0, []
    while nodeVals:
        startPoint = heapq.heappop(nodeVals)[1]
        allNodes.remove(startPoint)
        res.append(set())
        res[result].add(startPoint)
        DepthFirstSearch2(adj, startPoint, allNodes, res[result])
        nodeVals = list(filter(lambda x: x[1] in allNodes, nodeVals))
        result += 1

    for component in res:
        if len(component) > 1:
            print("res=", component)

    # AllCombined = set()
    # for x in res:
    #     AllCombined.update(x)
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
