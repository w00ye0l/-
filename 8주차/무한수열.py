def dfs(n):
    if n in dic:
        return dic[n]

    dic[n] = dfs(n // p) + dfs(n // q)
    # dfs(10000000) => dic[10000000] = dfs(3333333) + dfs(3333333)
    # dfs(3333333) => dic[3333333] = dfs(1111111) + dfs(1111111)
    # dfs(1111111) => dic[1111111] = dfs(370370) + dfs(370370)
    # ...
    # dfs(6) => dic[6] = dfs(6 // 3) + dfs(6 // 3)
    # dfs(2) => dic[2] = dfs(2 // 3) + dfs(2 // 3)
    # dfs(2) => dic[2] = dfs(0) + dfs(0)
    # dfs(0)일 때는 0이 dic에 있으므로 dic[2] = 1 + 1 = 2
    # 다시 순차적으로 위로 올라가면서 값들을 더해 원하는 값을 구할 수 있음
    print(n, dic[n])

    return dic[n]


n, p, q = map(int, input().split())

dic = {0: 1}

print(dfs(n))
