# 하샤드 수

def solution(x):
    x_list = list(str(x))
    if x % sum(map(int, x_list)) == 0:
        answer = True
    else:
        answer = False
    return answer