# 최댓값과 최솟값

def solution(s):
    answer = list(map(int, s.split(' ')))
    return str(min(answer)) + " " + str(max(answer))
