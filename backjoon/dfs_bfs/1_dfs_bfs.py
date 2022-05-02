import sys
from collections import deque

def dfs(n):

    print(n, end=' ')
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    n, m, v = map(int, sys.stdin.readline().split())
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        graph[i].sort()

    dfs(v)

    print()

    visited = [False] * (n+1)
    bfs(v)