from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]

    for e in edge:
        u, v = e[0], e[1]
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    queue.append(1)
    visited = [0] * (n + 1)
    visited[1] = 1

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj] = visited[cur] + 1
                queue.append(adj)

    answer = visited.count(max(visited))

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
