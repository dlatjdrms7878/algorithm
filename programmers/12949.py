# 행렬의 곱셈

import numpy as np

def solution(arr1, arr2):
    answer = np.matmul(np.array(arr1), np.array(arr2))
    return answer.tolist()

"""
def solution(arr1, arr2):
    return [[sum(n1*n2 for n1, n2 in zip(row1, col2)) for col2 in zip(*arr2)] for row1 in arr1]
"""