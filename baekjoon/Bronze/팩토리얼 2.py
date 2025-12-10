"""
Docstring for baekjoon.Bronze.팩토리얼 2
"""

N = int(input())

def fac(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fac(num-1)

print(fac(N))