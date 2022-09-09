# 문자열 내 p와 y의 개수

s = "pPoooyY"

def solution(s):
    s = s.lower()
    print(s)
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

solution(s)