# 올바른 괄호

def solution(s):
    left = 0
    for p in s:
        if left == 0 and p == ')':
            return False
        elif left != 0 and p == ')':
            left -= 1
        elif p == '(':
            left += 1
    if left == 0:
        return True
    else:
        return False