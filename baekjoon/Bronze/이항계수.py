# 조합
import math

N, K = map(int, input().split())

result = math.factorial(N) // math.factorial(N-K)
answer = result // math.factorial(K)

print(answer)