n = int(input())
gam = []
for i in range(n):
    gam.append(list(map(int, input().split())))

m = int(input())
order = []
for i in range(m):
    order.append(list(map(int, input().split())))

for i in range(m):
    if order[i][1] == 0:
        first = gam[order[i][0] - 1][:order[i][2]]
        second = gam[order[i][0] - 1][order[i][2]:]
        result = second + first
        gam[order[i][0] - 1] = result
    elif order[i][1] == 1:
        first = gam[order[i][0] - 1][:n - order[i][2]]
        second = gam[order[i][0] - 1][n - order[i][2]:]
        result = second + first
        gam[order[i][0] - 1] = result

sum_ = 0

for i in range(n // 2):
    for j in range(i, n - i):
        sum_ += gam[i][j]

for i in range(n // 2, n):
    for j in range(n - i - 1, i + 1):
        sum_ += gam[i][j]

print(sum_)
