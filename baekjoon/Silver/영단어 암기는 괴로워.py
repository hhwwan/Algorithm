"""
Docstring for baekjoon.Silver.영단어 암기는 괴로워
"""
from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_list = []

for i in range(N):
    word = input().strip()

    if len(word) >= M:
        word_list.append(word)

counter = Counter(word_list)

result = sorted(counter.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for w, cnt in result:
    print(w)