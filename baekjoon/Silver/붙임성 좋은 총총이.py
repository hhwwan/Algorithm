"""
Docstring for baekjoon.Silver.붙임성 좋은 총총이
"""

N = int(input())

rainbow = set()
rainbow.add('ChongChong')
for i in range(N):
    A, B = input().split()

    if A in rainbow:
        rainbow.add(B)
    elif B in rainbow:
        rainbow.add(A)

print(len(rainbow))