# 문자열 다루기 기본

def solution(s):
    if (6 == len(s) or 4 == len(s)) and s.isdigit():
        return True
    else:
        return False

"""
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
"""