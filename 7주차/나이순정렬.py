n = int(input())

user = []
for i in range(n):
    # 나이와 이름을 분해하여 입력 받기
    k, v = input().split()

    # 나이를 숫자로 변환, 입력 받은 순서 i를 같이 저장
    user.append((int(k), v, i))

# 나이(0번째)와 입력 받은 순서(2번째)를 기준으로 정렬
user.sort(key=lambda x: (x[0], x[2]))

# 나이(0번째)와 이름(1번째) 출력
for u in user:
    print(u[0], u[1])
