n = int(input())

# 시리얼 번호를 저장할 딕셔너리
sirial = {}

for _ in range(n):
    # 시리얼 번호를 입력
    temp = list(input())
    # 시리얼 번호의 길이 저장
    len_ = len(temp)

    # 시리얼 번호에 포함된 숫자들의 합
    sum_ = 0

    for t in temp:
        # 시리얼 번호에 포함된 숫자는 문자보다 아스키코드가 작음
        if ord(t) < ord('A'):
            # 숫자일 경우 합에 누적
            sum_ += int(t)

    # 길이와 합 리스트를 시리얼 번호인 문자열을 키로 갖는 딕셔너리에 추가
    sirial[''.join(temp)] = [len_, sum_]

# 길이([1][0]번째), 합([1][1]번째), 사전순([0]번째)의 순서대로 정렬
sirial = sorted(sirial.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

# 시리얼 번호(0번째)를 출력
for s in sirial:
    print(s[0])
