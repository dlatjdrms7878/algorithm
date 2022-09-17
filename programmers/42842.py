# 카펫

def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0 and brown+yellow == (yellow//i+2) * (i+2):
            return [yellow//i+2, i+2]