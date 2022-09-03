n = int(input())
m = int(input())

if m == 0:
    print(len(str(n)))
else:
    broken = list(map(int, input().split()))

    min_ = abs(100 - n)

    for num in range(1000001):
        num = str(num)

        cnt = 0
        for j in num:
            if int(j) in broken:
                break
            elif cnt == len(num) - 1:
                min_ = min(min_, abs(int(num) - n) + len(num))

            cnt += 1

    print(min_)
