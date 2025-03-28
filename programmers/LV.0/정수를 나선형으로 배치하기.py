"""
양의 정수 n이 매개변수로 주어집니다. 
n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""

d = [[0, 1],[1, 0],[0, -1],[-1, 0]]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    c = 1
    dt = 0

    while c <= n * n:
        answer[x][y] = c
        c+=1
        xx, yy = x + d[dt][0], y + d[dt][1]
        if 0 <= xx < n and 0 <= yy < n:
            if answer[xx][yy] != 0:
                dt = (dt + 1) % 4
                x, y = x + d[dt][0], y + d[dt][1]
            else:
                x, y = xx, yy
        else:
            dt = (dt + 1) % 4
            x, y = x + d[dt][0], y + d[dt][1]


    return answer