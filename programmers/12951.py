# JadenCase 문자열 만들기

def solution(s):
    s = s.lower()
    prev = ' '
    answer = ''
    for w in s:
        if prev == ' ' and w != ' ':
            w = w.upper()
        answer += w
        prev = w
    return answer