# 나머지가 1이 되는 수 찾기

n = int(input())

def solution(n):
    answer = 0
    while True:
        answer += 1
        if n % answer == 1:
            break
    return answer

print(solution(n))

"""
def solution(n):
    return [x for x in range(1, n+1) if n%x == 1][0]
"""