# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    arr.sort()
    answer = [x for x in arr if x % divisor == 0]
    if answer:
        return answer
    else:
        return [-1]

"""
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""