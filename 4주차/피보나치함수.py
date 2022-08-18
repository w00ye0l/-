t = int(input())

fibo = [[] for _ in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]

for i in range(2, 41):
    a, b = fibo[i - 1][0] + \
        fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]
    fibo[i] = [a, b]

for _ in range(t):
    n = int(input())

    print(fibo[n][0], fibo[n][1])
