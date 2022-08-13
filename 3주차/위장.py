def solution(clothes):
    answer = 1

    dic = {}
    for clo in clothes:
        if not clo[1] in dic:
            dic[clo[1]] = 2
        else:
            dic[clo[1]] += 1

    for k, v in dic.items():
        answer *= v

    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
