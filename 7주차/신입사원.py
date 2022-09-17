import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    # 신입사원의 등수 입력
    emp = []
    for i in range(n):
        emp.append(list(map(int, input().split())))

    # 등수 정렬
    emp.sort()

    # 첫 번째 시험 등수는 뒤로 갈수록 낮아짐
    comp = emp[0][1]
    # 첫 번째 사람은 무조건 합격(인원수 1)
    cnt = 1

    # 반복문을 돌며 두 번째 등수 비교
    for i in range(1, n):
        # 다음 사람과 두 번째 시험 등수를 비교해서 다음 사람의 등수가 낮으면
        if comp > emp[i][1]:
            # 인원수를 늘리고
            cnt += 1
            # 두 번째 시험 등수 기준을 바꿈
            comp = emp[i][1]
            # 첫 번째 시험은 뒤로 갈수록 낮아지기 때문에 두 번째 등수가 높아야 합격

    print(cnt)
