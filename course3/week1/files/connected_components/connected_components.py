#Uses python3
import sys


def getNeighborhood(adj, point, reached):
    return [p for p in adj[point] if p not in reached]


def breathFirstSearch(adj, start):
    neighborhood = getNeighborhood(adj, start, traversed)
    Allneighborhood.extend(neighborhood)
    traversed.extend(neighborhood)
    if Allneighborhood == []:
        return
    else:
        newPoint = Allneighborhood.pop()
        breathFirstSearch(adj, newPoint)

def getAllNodes(adj):
    allNodes = []
    for node in adj:
        for node_next in node:
            if node_next not in allNodes:
                allNodes.append(node_next)
    return allNodes


def number_of_components(adj, n):
    global traversed, Allneighborhood
    if n < 1:
        return 0
    result = 1
    Allneighborhood = []
    allNodes = getAllNodes(adj)
    connectedCount = len(allNodes)
    #print("allNodes=",allNodes,"L=",len(allNodes))
    if allNodes == []:
        return n
    traversed = [allNodes[0]]
    startPoint = allNodes[0]
    while len(traversed) < n:
        breathFirstSearch(adj, startPoint)
        allNodes = [i for i in allNodes if i not in traversed]
        if allNodes == []:
            break
        startPoint = allNodes[0]
        traversed.append(startPoint)
        result += 1
    return result+n-connectedCount


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
    print(number_of_components(adj, n))
