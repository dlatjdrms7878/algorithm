# 정수 내림차순으로 배치하기

def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    return int(''.join(n_list))