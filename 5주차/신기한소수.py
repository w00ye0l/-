def prime(a):
    if a < 2:
        return False

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in [1, 3, 7, 9]:
            new_num = num * 10 + i
            if prime(new_num):
                dfs(new_num)


n = int(input())

for i in [2, 3, 5, 7]:
    dfs(i)
