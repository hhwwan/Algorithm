"""
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 
두 소수의 순서만 다른 것은 같은 파티션이다.
"""

# 내가 푼 것 -> 시간 초과 아마도 에라토스테네스체 써야할듯
# 소수 판별기
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    x = int(input())
    tmp = 0

    for i in range(2, x//2 + 1):
        if is_prime(i) and is_prime(x-i):
            tmp += 1
    print(tmp)

# 에라토스테네스체
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

T = int(input())

for _ in range(T):
    x = int(input())
    tmp = 0

    for i in range(2, x//2 + 1):
        if prime_list[i] and prime_list[x-i]:
            tmp += 1
    print(tmp)
