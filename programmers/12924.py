# 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            answer += 1
    
    return answer

"""
def solution(n):
    return len([i for i in range(1, num+1, 2) if num % i is 0])
"""