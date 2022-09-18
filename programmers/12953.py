# N개의 최소공배수

import math

def solution(arr):
    lcm = arr[0]
    for n in arr[1:]:
        lcm = lcm * n // math.gcd(lcm, n)
        
    return lcm
        