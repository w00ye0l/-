from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))

oper = ['+', '-', '*', '/']
oper_cnt = list(map(int, input().split()))

l_oper = []
for i in range(4):
    for _ in range(oper_cnt[i]):
        l_oper.append(oper[i])

pro_oper = list(permutations(l_oper, len(l_oper)))
# print(len(pro_oper))

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

# from itertools import permutations
# from collections import deque

# n = int(input())

# arr = deque(list(map(int, input().split())))

# oper = ['+', '-', '*', '//']
# oper_cnt = list(map(int, input().split()))

# l_oper = []
# for i in range(4):
#     if oper_cnt[i]:
#         for _ in range(oper_cnt[i]):
#             l_oper.append(oper[i])

# pro_oper = list(permutations(l_oper, len(l_oper)))

# answer = []
# max_ = -1e9
# min_ = 1e9

# for p in pro_oper:
#     temp = deque(arr)
#     modi = ""
#     p = deque(p)

#     while len(p):
#         modi += str(temp.popleft())
#         modi += p.popleft()

#     modi += str(temp.popleft())
#     if max_ < eval(modi):
#         max_ = eval(modi)
#     elif min_ > eval(modi):
#         min_ = eval(modi)

# print(max_)
# print(min_)
