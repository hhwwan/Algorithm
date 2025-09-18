"""
2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
"""

while True:
    try:
        n = int(input())
    except:
        break
    
    num = 1
    cnt = 1

    while True:
        if num % n != 0:
            num = num * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)

# 더 빠른코드
while True:
    try:
        n = int(input())
    except:
        break

    remain = 1
    cnt = 1

    while remain % n != 0:
        remain = (remain * 10 + 1) % n
        cnt += 1
    
    print(cnt)