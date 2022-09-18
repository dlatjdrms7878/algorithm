# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, val in enumerate(citations):
        if val < idx+1:
            break
        answer = idx+1
    return answer

"""
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))
"""