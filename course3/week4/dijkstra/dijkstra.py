#Uses python3

import sys
import heapq


def getNeighbourhood(neighbours, cost, pqueue, currectD, optimized):
    goodNeighboursIdx = [idx for idx in range(len(neighbours))
                         if neighbours[idx] not in optimized]
    for idx in goodNeighboursIdx:
        heapq.heappush(pqueue, (cost[idx]+currectD, neighbours[idx]))
    print("pqueue=", pqueue)
    return goodNeighboursIdx


def distance(adj, cost, s, t, maxWeight):
    if s == t:
        return 0
    pqueue = [(0, s)]
    optimized = set([s])
    distance = [maxWeight*len(adj)]*len(adj)
    distance[s] = 0
    while pqueue:
        nextPoint = pqueue.pop(0)
        neighbours = adj[nextPoint[1]]
        currectD = distance[nextPoint[1]]
        costs = cost[nextPoint[1]]
        print("nextpoint=", nextPoint, "currectD=", currectD)
        neighboursIdx = getNeighbourhood(neighbours, costs, pqueue,
                                         currectD, optimized)
        for ne in neighboursIdx:
            distance[ne] = min(distance[ne], costs[ne]+currectD)
        optimized.add(nextPoint[1])
        if t in optimized:
            return distance[nextPoint[1]]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m): 3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    maxWeight = 0

    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        maxWeight = max(maxWeight, w)
    s, t = data[0] - 1, data[1] - 1

    print(distance(adj, cost, s, t, maxWeight))
