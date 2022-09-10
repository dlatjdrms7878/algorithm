# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = [x*(i+1) for i in range(n)]
    return answer