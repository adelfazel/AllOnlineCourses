#Uses python3
import sys
import math
import heapq


def getParent(tableIdx, parents):
    children = []
    root = tableIdx
    while root != parents[root]:
        children.append(root)
        root = parents[root]
    for child in children:
        parents[child] = root
    return root


def merge(destination, source, parent, rank):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False
    global ans
    if rank[realDestination] > rank[realSource]:
        parent[realSource] = parent[realDestination]
        rank[realSource] = 0
    else:
        parent[realDestination] = parent[realSource]
        rank[realDestination] = 0
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1
    return True


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def minimum_distance(x, y, n):
    AllPoints = list(zip(x, y))
    AllDistances = []
    for p1Idx in range(n-1):
        p1 = AllPoints[p1Idx]
        for p2Idx in range(p1Idx+1, n):
            p2 = AllPoints[p2Idx]
            heapq.heappush(AllDistances, (distance(p1, p2), (p1, p2)))
    result, iter = 0., 1

    ranks = [1] * n
    parents = list(range(0, n))

    while iter < n:
        nextDist, nextEdge = heapq.heappop(AllDistances)
        print("iter=", iter, "explored=", "nextEdge=", nextEdge)
        if getParent(nextEdge[0], parents) != getParent(nextEdge[1], parents):

            result += nextDist
            iter += 1

    return result



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
