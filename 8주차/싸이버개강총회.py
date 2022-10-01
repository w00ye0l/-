import sys

input = sys.stdin.readline

s, e, q = input().split()

s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])

dic = {}
while True:
    try:
        t, name = input().split()
        t = int(t[:2] + t[3:])

        if t <= s:
            dic[name] = 1
        elif e <= t <= q and name in dic:
            dic[name] = 0
    except:
        break

print(list(dic.values()).count(0))

# import sys

# input = sys.stdin.readline

# s, e, q = input().split()

# s_h, s_m = int(s[:2]), int(s[3:])
# e_h, e_m = int(e[:2]), int(e[3:])
# q_h, q_m = int(q[:2]), int(q[3:])

# dic = {}
# while True:
#     try:
#         t, name = input().split()
#         t_h, t_m = int(t[:2]), int(t[3:])

#         if not name in dic:
#             if t_h < s_h:
#                 dic[name] = 1
#             elif t_h == s_h and t_m <= s_m:
#                 dic[name] = 1
#         else:
#             if e_h < t_h < q_h:
#                 dic[name] = 0
#             elif e_h == t_h and e_m <= t_m:
#                 dic[name] = 0
#             elif t_h == q_h and t_m <= q_m:
#                 dic[name] = 0
#     except:
#         break

# print(list(dic.values()).count(0))
