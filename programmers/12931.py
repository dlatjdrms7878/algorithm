# 자릿수 더하기

n = input()

def solution(n):
    answer = 0

    for i in range(len(n)):
        answer += int(n[i])

    return answer

print(solution(n))

"""
def solution(n):
    return sum([int(i) for i in str(n)])
"""