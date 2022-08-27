from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1, q2 = deque(queue1), deque(queue2)

    l = len(q1)
    sum_q1, sum_q2 = sum(q1), sum(q2)

    if sum_q1 > sum_q2:
        max_q, min_q = q1, q2
    elif sum_q1 < sum_q2:
        max_q, min_q = q2, q1
    else:
        return answer

    s_max, s_min = sum(max_q), sum(min_q)

    while max_q and min_q and answer < 3 * l:
        if s_max < s_min:
            max_q, min_q = min_q, max_q
            s_max, s_min = s_min, s_max

        elif s_max == s_min:
            return answer

        p = max_q.popleft()
        s_max -= p

        min_q.append(p)
        s_min += p

        answer += 1

    return -1


print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
# print(solution([1, 1], [1, 5]))
