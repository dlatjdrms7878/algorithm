# 정수 제곱근 판별

import math

n = int(input())

def solution(n):
    sqrt = n ** 0.5

    if sqrt % 1 == 0:
        return int((sqrt + 1) ** 2)
    else:
        return -1

print(solution(n))