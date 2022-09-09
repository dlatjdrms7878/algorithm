# 짝수와 홀수

num = int(input())

def solution(num):
    if num == 0 or num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

print(solution(num))

"""
def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"
"""