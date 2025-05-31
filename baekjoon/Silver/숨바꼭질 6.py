"""
수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.

수빈이는 걸어서 이동을 할 수 있다. 
수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 
수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.

모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.

동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다.

가능한 D값의 최댓값을 출력한다.
"""

import math

N, S = map(int,input().split())
bro = list(map(int,input().split()))

distance = [abs(x - S) for x in bro]

answer = distance[0]

for i in range(1, N):
    answer = math.gcd(answer, distance[i])

print(answer)