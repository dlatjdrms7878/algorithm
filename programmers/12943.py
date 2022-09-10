# 콜라츠 추측

def solution(num):
    answer = 0
    return recursive(num, answer)

def recursive(num, answer):
    if num == 1:
        return answer
    
    if answer == 500:
        return -1
    
    if num % 2 == 0:
        return recursive(num / 2, answer + 1)
    else:
        return recursive(num * 3 + 1, answer + 1)
        