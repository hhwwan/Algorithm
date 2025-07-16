"""
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 
이때 x를 y로 만들 수 없다면 -1을 return 해주세요.
"""

from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    
    # 방문한 기록
    visited = set()
    visited.add(x)
    
    while queue:
        # 맨 앞에 있는걸 하나씩 꺼내서 확인
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        for next_num in (current + n, current * 2, current * 3):
            if next_num > y:
                continue
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))
    
    return -1