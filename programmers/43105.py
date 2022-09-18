# 정수 삼각형

def solution(triangle):
    for t_idx, t_val in enumerate(triangle[1:], start=1):
        for f_idx, f_val in enumerate(t_val):
            if f_idx == 0:
                triangle[t_idx][f_idx] += triangle[t_idx-1][f_idx]
            elif f_idx == len(t_val)-1:
                triangle[t_idx][f_idx] += triangle[t_idx-1][f_idx-1]
            else:
                triangle[t_idx][f_idx] += max(triangle[t_idx-1][f_idx-1], triangle[t_idx-1][f_idx])

    return max(triangle[len(triangle)-1])