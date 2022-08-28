from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))

oper = ['+', '-', '*', '/']
oper_cnt = list(map(int, input().split()))

l_oper = []
for i in range(4):
    for _ in range(oper_cnt[i]):
        l_oper.append(oper[i])

pro_oper = list(set(permutations(l_oper, len(l_oper))))

answer = []
for p in pro_oper:
    result = arr[0]

    for i in range(len(arr) - 1):
        if p[i] == '+':
            result += arr[i + 1]
        elif p[i] == '-':
            result -= arr[i + 1]
        elif p[i] == '*':
            result *= arr[i + 1]
        elif p[i] == '/':
            result = int(result / arr[i + 1])

    answer.append(result)

print(max(answer))
print(min(answer))
