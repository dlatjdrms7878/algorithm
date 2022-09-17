# 영어 끝말잇기

def solution(n, words):
    prev = words[0][0]
    for idx, word in enumerate(words):
        if word in words[:idx]:
            return [idx%n+1, idx//n+1]
        if word[0] != prev:
            return [idx%n+1, idx//n+1]
        prev = word[-1]
    return [0, 0]