n = int(input())

def solution(n):
    answer = []
    for i in range(0, len(str(n))):
        answer.append(n % 10)
        n = n // 10
    
    return answer

print(solution(n))

"""
def solution(n):
    return list(map(int, reversed(str(n))))

def solution(n):
    return [int(i) for i in str(n)][::-1]
"""