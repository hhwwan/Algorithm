"""
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 
이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.
"""
# # 내가 푼 것 -> 시간초과
while (1):
    n = int(input())
    if n == 0:
        break
    result = None

    # 2부터 n의 절반까지 반복하며 소수 찾기
    for i in range(2, n//2 + 1):
        tmp = True

        # i가 소수인지 확인
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                tmp = False
                break

        if tmp:
            # n-i가 소수인지
            for k in range(2, int((n-i)**0.5) + 1):
                if (n-i) % k == 0:
                    tmp = False
                    break

            if tmp:
                # 조건을 만족하는 소수쌍 저장
                result = (i, n-i) # 가장 마지막에 발견된 소수 쌍이 b-a가 가장 큼

    if result:
        a, b = result
        print(n, '=', a, '+', b)
    else:
        print("Goldbach's conjecture is wrong.")

# 에라토스테네스의 체로 미리 소수 리스트 만들어서 풀기
import sys
input = sys.stdin.readline

def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

MAX = 1000000
prime_list = prime(MAX)

# 골드바흐 추측
while 1:
    n = int(input())
    if n == 0:
        break

    for i in range(3, int(n/2)+1, 2): 
        if prime_list[i] and prime_list[n-i]:
            print(f"{n} = {i} + {n-i}")
            break

    else:
        print("Goldbach's conjecture is wrong.")