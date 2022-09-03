from collections import deque


def dfs(v, visited):
    visited[v] = 1
    print(v, end=' ')

    for adj in graph[v]:
        if visited[adj] == 0:
            dfs(adj, visited)


def bfs(v):
    visited = [0] * (n + 1)

    queue = deque()
    queue.append(v)
    result = [v]
    visited[v] = 1

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if visited[adj] == 0:
                queue.append(adj)
                visited[adj] = 1
                result.append(adj)

    return result


n, m, v = list(map(int, input().split()))
visited = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


dfs(v, visited)
print()
print(*bfs(v))
