from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    now_status = sum(bridge)
    truck_weights = deque(truck_weights)

    while bridge:
        answer += 1
        arrive = bridge.popleft()
        now_status -= arrive

        if truck_weights:
            if now_status + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                now_status += t
            else:
                bridge.append(0)

    return answer


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
