import math


def solution(fees, records):
    answer = []
    park = {}
    fee_dic = {}

    for r in records:
        t, car_num, sta = list(r.split())
        hh, mm = t.split(':')
        hh, mm = map(int, (hh, mm))

        if sta == 'IN':
            if not car_num in park:
                park[car_num] = [hh, mm, 0, 0]
            else:
                park[car_num][:3] = [hh, mm, 0]
        elif sta == 'OUT':
            in_hh, in_mm = park[car_num][:2]
            park[car_num][2] = 1

            p_hh = hh - in_hh
            p_mm = mm - in_mm

            park[car_num][3] += p_hh * 60 + p_mm

    for k, v in park.items():
        if v[2] == 0:
            in_hh, in_mm = v[:2]
            v[2] = 1
            p_hh = 23 - in_hh
            p_mm = 59 - in_mm

            v[3] += p_hh * 60 + p_mm

        if v[3] <= fees[0]:
            fee_dic[k] = fees[1]
        else:
            fee_dic[k] = fees[1] + \
                (math.ceil((v[3] - fees[0]) / fees[2]) * fees[3])

    fee_dic = sorted(fee_dic.items(), key=lambda x: (x[0], x[1]))

    for f in fee_dic:
        answer.append(f[1])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
