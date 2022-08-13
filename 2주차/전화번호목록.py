def solution(phone_book):
    n = len(phone_book)

    phone_book.sort()
    answer = True

    for i in range(n - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    return answer


###############################

# def solution(phone_book):
#     answer = True
#     n = len(phone_book)

#     phone_book.sort()

#     for i in range(n - 1):
#         if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
#             answer = False
#             break

#     return answer

# 효율성 0

# def solution(phone_book):
#     answer = True
#     n = len(phone_book)

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 pass
#             elif phone_book[j].startswith(phone_book[i]):
#                 answer = False
#                 break

#     return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
