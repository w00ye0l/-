def solution(record):
    answer = []
    name = {}

    for r in record:
        order = r.split()
        if order[0] == 'Enter' or order[0] == 'Change':
            name[order[1]] = order[2]

    for r in record:
        order = r.split()
        if order[0] == 'Enter':
            answer.append(f"{name[order[1]]}님이 들어왔습니다.")
        elif order[0] == 'Leave':
            answer.append(f"{name[order[1]]}님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
