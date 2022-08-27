def solution(genres, plays):
    answer = []

    l = len(genres)

    dic = {}
    for i in range(l):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]

    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

    al = []
    for d in dic:
        if d[0] not in al:
            al.append(d[0])
    lists = []
    for i in range(l):
        lists.append([genres[i], plays[i]])

    lists = sorted(lists, key=lambda x: (-x[1], x[0]))

    for a in al:
        cnt = 0

        for i in range(l):
            if a == lists[i][0]:
                cnt += 1
                answer.append(plays.index(lists[i][1]))
                plays[plays.index(lists[i][1])] = -1

            if cnt == 2:
                break

    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))
