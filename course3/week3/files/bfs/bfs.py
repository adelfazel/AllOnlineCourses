#Uses python3

import sys
import queue


def distance(adj, s, t, n):
    queued = [s]
    dist = [-1]*n
    dist[s] = 0
    while queued:
        st = queued.pop(0)
        neighbors = [x for x in adj[st] if dist[x] == -1]
        if t in neighbors: return dist[st]+1
        for ne in neighbors: dist[ne] = dist[st]+1
        queued.extend(neighbors)

    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t, n))
