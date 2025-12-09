"""
Docstring for baekjoon.Silver.통계학
"""
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

avg = sum(num_list) / N

num_sort = sorted(num_list)
median = num_sort[N//2]

counter = Counter(num_list)
max_freq = max(counter.values())
candidates = [n for n, cnt in counter.items() if cnt == max_freq]
candidates.sort()
if len(candidates) == 1:
    frequent = candidates[0]
else:
    frequent = candidates[1]

range = num_sort[-1] - num_sort[0]

print(int(round(avg, 0)))
print(median)
print(frequent)
print(range)