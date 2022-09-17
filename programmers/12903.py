# 가운데 글자 가져오기

def solution(s):
    print(len(s))
    if len(s) % 2 == 0:
        answer = s[len(s)//2-1:len(s)//2+1]
    else:
        answer = s[len(s)//2]
    return answer

"""
def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]
"""