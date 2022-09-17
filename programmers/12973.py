# 짝지어 제거하기

def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    stack = [s[0]]
    
    for i in s[1:]:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return 0 if len(stack) else 1