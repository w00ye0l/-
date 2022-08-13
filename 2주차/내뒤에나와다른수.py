import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
result = []
idx1, idx2 = 0, 1

while idx1 <= idx2:
    if idx1 == n - 1:
        break
    if numbers[idx1] != numbers[idx2]:
        result += [idx2 + 1] * (idx2 - idx1)
        idx1 = idx2
        idx2 += 1
    elif idx2 == n - 1 and numbers[idx1] == numbers[idx2]:
        result += [-1] * (idx2 - idx1)
        break
    elif numbers[idx1] == numbers[idx2]:
        idx2 += 1

result.append(-1)

print(*result)


########################

# input = sys.stdin.readline

# n = int(input())

# numbers = list(map(int, input().split()))
# result = []

# for i in range(n):
#     for j in range(i + 1, n):
#         if numbers[i] != numbers[j]:
#             result.append(j + 1)
#             break
#     else:
#         result.append(-1)

# print(*result)
