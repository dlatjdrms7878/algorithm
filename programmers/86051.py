# 없는 숫자 더하기

def solution(numbers):
    all = set(range(1, 10))
    answer = sum(all - set(numbers))
    return answer

"""
def solution(numbers):
    return 45 - sum(numbers)
"""