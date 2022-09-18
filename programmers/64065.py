# 튜플

def solution(s):
    answer = []
    arr = s[2:-2].split('},{')
    arr = [i.split(',') for i in arr]
    arr.sort(key=len)
    answer = []
    for idx, val in enumerate(arr):
        if idx == 0:
            answer += arr[0]
        else:
            answer += list(set(val) - set(arr[idx-1]))
    return list(map(int, answer))

    """
    def solution(s):
        s = Counter(re.findall('\d+', s))
        return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
    """