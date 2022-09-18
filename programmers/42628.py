# 이중우선순위큐

import heapq

def solution(operations):
    heap = []
    max_heap = []
    min_heap = []
    for op in operations:
        option, num = op.split()
        if option == 'I':
            heapq.heappush(heap, int(num))
        else:
            if heap:
                if num == '1':
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)
    if heap:
        return [*heapq.nlargest(1, heap), heapq.heappop(heap)]
    else:
        return [0, 0]

print(solution(["I 2", "I 4", "D -1", "I 1", "D 1"]))