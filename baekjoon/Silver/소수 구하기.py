"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""

M, N = list(map(int,input().split()))

for i in range(M,N+1):
    if i < 2:
        continue
    tmp = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            tmp = False
            break
    if tmp:
        print(i)