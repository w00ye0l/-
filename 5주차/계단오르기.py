n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

result = []

if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0] + arr[1], arr[1]))
elif n == 3:
    print(max(arr[0] + arr[2], arr[1] + arr[2]))
else:
    result.append(arr[0])
    result.append(max(arr[0] + arr[1], arr[1]))
    result.append(max(arr[0] + arr[2], arr[1] + arr[2]))

    for i in range(3, n):
        result.append(max(result[i - 2] + arr[i],
                          result[i - 3] + arr[i - 1] + arr[i]))

    print(result.pop())
