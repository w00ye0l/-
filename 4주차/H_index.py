def solution(citations):
    answer = 0

    citations.sort()

    i = 0
    while True:
        cnt = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                cnt += 1

        if i > cnt:
            answer = i - 1
            break

        i += 1

    return answer


print(solution([3, 0, 6, 1, 5]))
