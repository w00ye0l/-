# 민식어 사전을 만들어 순서를 기록
# ng는 x로 대체
dic = {
    'a': 1,
    'b': 2,
    'k': 3,
    'd': 4,
    'e': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'l': 9,
    'm': 10,
    'n': 11,
    'x': 12,
    'o': 13,
    'p': 14,
    'r': 15,
    's': 16,
    't': 17,
    'u': 18,
    'w': 19,
    'y': 20
}

n = int(input())

temp = []
for _ in range(n):
    s = input()

    # 입력 받은 문자열을 한 글자씩 끊어서 판단하기 때문에 두 글자인 'ng'를 'x'로 대체
    s = s.replace('ng', 'x')

    # 글자의 순서를 계산하기 위해 사전 순서(숫자)를 입력 받을 리스트를 만듦
    cnt = []
    for i in s:
        cnt.append(dic[i])

    # 입력받은 단어와 숫자로 변환한 리스트를 동시에 저장
    temp.append([s, cnt])

# 숫자로 변환한 리스트를 기준으로 정렬
temp.sort(key=lambda x: x[1])

# 단어(0번째)와 숫자리스트(1번째)를 동시에 입력 받았기 때문에 단어만 출력
for t in temp:
    # 단어에 있는 'x'를 다시 'ng'로 변환
    t[0] = t[0].replace('x', 'ng')

    print(t[0])
