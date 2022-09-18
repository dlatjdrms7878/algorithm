# 괄호 회전하기

def solution(s):
    answer = 0
    left = ['(', '{', '[']
    right = [')', '}', ']']
    for idx, val in enumerate(s):
        if val in ['(', '{', '[']:
            stack = [val]
            for i in range(1, len(s)):
                if s[(idx+i)%len(s)] in left:
                    stack.append(s[(idx+i)%len(s)])
                elif s[(idx+i)%len(s)] in right:
                    if not stack:
                        break
                    if left.index(stack[-1]) == right.index(s[(idx+i)%len(s)]):
                        stack.pop()
                    else:
                        break
                    
            else:
                if not stack:
                    answer += 1
    
    return answer

"""
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer
"""