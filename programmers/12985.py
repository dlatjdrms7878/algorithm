# 예상 대진표

def solution(n,a,b):
    answer = 0
    a, b = min(a, b), max(a, b)
    while True:
        answer += 1
        if b-a==1 and b%2==0:
            return answer
        a = (a+1)//2
        b = (b+1)//2

    return answer

"""
def solution(n, a, b):
    return ((a-1)^(b-1)).bit_length()
"""