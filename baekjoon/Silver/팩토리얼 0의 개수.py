"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""

N = int(input())
tmp = 1
answer = 0

for i in range(2, N+1):
    tmp *= i

for j in str(tmp)[::-1]:
    if j == '0':
        answer += 1
    else:
        break

print(answer)