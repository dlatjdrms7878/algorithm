# 약수의 합

n = int(input())

def solution(n):
    answer = 0

    for i in range(1, n//2 + 1):
        if n % i == 0:
            answer += i

    answer += n

    return answer

print(solution(n))

"""
def solution(num):
    return num + sum([i for i in range(1, (num // 2 ) + 1 if num % i == 0])
"""