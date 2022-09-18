# 위장

from itertools import combinations
import math

def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        item, category = cloth
        if category in clothes_dict:
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 2
    return math.prod(clothes_dict.values()) - 1