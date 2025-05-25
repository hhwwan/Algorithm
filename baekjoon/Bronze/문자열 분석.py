"""
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
"""

import sys
input = sys.stdin.read

N = input().splitlines()

for data in N:
    answer = [0,0,0,0]

    for i in data:
        if i.islower():
            answer[0] += 1
        elif i.isupper():
            answer[1] += 1
        elif i.isdigit():
            answer[2] += 1
        elif i == ' ':
            answer[3] += 1

    print(' '.join(map(str, answer)))