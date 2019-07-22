#Uses python3
import sys

allGone=set()
def getAllNodes(adj, n):
    allConnectedNodes = set()
    allNodes = set(range(n))
    for node in adj:
        for node_next in node:
            if node_next not in allConnectedNodes:
                allConnectedNodes.add(node_next)
    allNodes.difference_update(allConnectedNodes)
    return (allNodes, allConnectedNodes)



def DepthFirstSearch(adj, startPoint, orderedPath,allConnectedNodes):
    neighborhoodlocal = set(x for x in adj[startPoint] if x in allConnectedNodes)
    while neighborhoodlocal:
        nextNode = neighborhoodlocal.pop()
        DepthFirstSearch(adj, nextNode, orderedPath, allConnectedNodes)
        neighborhoodlocal = set(x for x in adj[startPoint] if x in allConnectedNodes)    
    orderedPath.append(startPoint)
    allConnectedNodes.discard(startPoint)




    #allGone.add(startPoint)


def toposort(adj, n):
    if len(adj) < 2:
        return [0]
    unconnectedNodes, allConnectedNodes = getAllNodes(adj, n)
    orderedPath = []

    while allConnectedNodes:
        startPoint = allConnectedNodes.pop()
        DepthFirstSearch(adj, startPoint, orderedPath, allConnectedNodes)

    orderedPath.extend(unconnectedNodes)
    orderedPath.reverse()
    return orderedPath


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [set() for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].add(b - 1)
    order = toposort(adj, n)
    for x in order:
        print(x + 1, end=' ')
