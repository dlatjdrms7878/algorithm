# 최고의 집합

def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n for i in range(n)]
    for i in range(1, s%n+1):
        answer[-i] += 1
    
    return answer