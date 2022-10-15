import heapq
import sys

input = sys.stdin.readline

n = int(input())

course = []

for _ in range(n):
    s, t = map(int, input().split())

    course.append((s, t))

course.sort()

heap = []
heapq.heappush(heap, course[0][1])  # 가장 시작이 빠른 수업의 끝나는 시간을 저장

for i in range(1, n):
    if course[i][0] < heap[0]:  # 힙에 저장된 시간이 시작하는 시간이 작으면 새로 저장
        heapq.heappush(heap, course[i][1])
    else:  # 시작하는 시간이 힙에 저장되는 시간보다 크면 끝나는 시간으로 바꿔줌
        heapq.heapreplace(heap, course[i][1])

print(len(heap))
