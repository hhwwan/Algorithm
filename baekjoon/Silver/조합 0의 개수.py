"""
(n/m)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
"""

# 조합의 개수를 구하고 0을 일일히 셈 -> 시간초과
import math

n,m = map(int, input().split())
answer = 0

tmp = math.comb(n, m)

for i in str(tmp)[::-1]:
    if i == '0':
        answer += 1
    else:
        break

print(answer)

# 0의 개수만 세기
def count_factor(n, k):
    """n! 안에 있는 k(=2 또는 5)의 개수를 센다"""
    count = 0
    while n >= k:
        n //= k
        count += n
    return count

n, m = map(int, input().split())

# nCm = n! / (m! * (n - m)!)
# 따라서 전체 2, 5의 개수를 각각 구해서
# 남은 10의 개수를 세면 됨

two = count_factor(n, 2) - count_factor(m, 2) - count_factor(n - m, 2)
five = count_factor(n, 5) - count_factor(m, 5) - count_factor(n - m, 5)

print(min(two, five))