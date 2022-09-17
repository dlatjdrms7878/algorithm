# 다음 큰 숫자

def solution(n):
    bin_n = bin(n)[2:]
    cnt = bin_n.count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt:
            return n