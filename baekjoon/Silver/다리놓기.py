import math

T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    result = math.factorial(M) // math.factorial(M-N)
    result //= math.factorial(N)

    print(result)