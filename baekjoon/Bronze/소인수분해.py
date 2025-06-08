"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""

N = int(input())

while True:
    for i in range(2, N + 1):
        if N % i == 0:
            print(i)
            N //= i
            break
    if N == 1:
        break