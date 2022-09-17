# 음양 더하기

def solution(absolutes, signs):
    signs = list(map(lambda x: 1 if x else -1, signs))
    return sum([a*s for a, s in zip(absolutes, signs)])

"""
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""