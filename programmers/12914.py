# 멀리 뛰기

import math

def solution(n):
    answer = 0
    a = n // 2 + 1
    n1, n2 = n, 0
    for i in range(a):
        answer += math.factorial(n-i) // (math.factorial(n1)*math.factorial(n2))
        n1 -= 2
        n2 += 1
    
    return answer % 1234567
# n칸 뛰는 경우는 n-1칸 뛰는 경우에 1칸을 추가, n-2칸 뛰는 경우에 2칸을 추가 => 피보나치 수열
"""
def solution(n):
    a, b = 1, 2
    if num == 1:
        return 1
    
    for i in range(2, num):
        a, b = b, a + b
    return b % 1234567
"""
