n = int(input())

num = list(map(int, input().split()))

# 입력받은 좌표들을 중복 제거하여 정렬
ch = list(set(num))
ch.sort()

# 숫자들의 등수를 0부터 dic에 저장
dic = {}
i = 0
for c in ch:
    # 등장 순서가 순위이므로 순위를 저장하고
    dic[c] = i
    # 다음 순위를 위해 1을 증가시킴
    i += 1

# 좌표들의 순위를 한줄에 출력
for n in num:
    print(dic[n], end=' ')
