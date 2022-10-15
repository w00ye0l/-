import heapq

n, m = map(int, input().split())
con = [0] * m  # 콘센트 개수만큼 빈칸 만들기

charge = list(map(int, input().split()))
charge.sort()  # 오름차순 정렬

for i in range(n):
    temp = heapq.heappop(con)  # 가장 작은 값을 뽑아서

    temp += charge.pop()  # 가장 큰 값을 더함
    heapq.heappush(con, temp)  # 다시 힙에 넣기
    print(con)

print(max(con))
