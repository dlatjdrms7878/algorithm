# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += len(s)
        s = [x for x in s if x == '1']
        answer[1] -= len(s)
        s = bin(len(s))[2:]
        answer[0] += 1

    return answer