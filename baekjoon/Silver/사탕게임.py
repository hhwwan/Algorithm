"""
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N * N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
"""

N = int(input())
candy = [list(input()) for _ in range(N)]

# 최대길이 구하는 함수
def check_length():
    max_length = 1

    for k in range(N):
        length = 1
        # 오른쪽이 같은 경우
        for x in range(N):
            if x + 1 < N and candy[k][x] == candy[k][x + 1]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
        # 밑쪽이 같은 경우
        for y in range(N):
            if y + 1 < N and candy[y][k] == candy[y + 1][k]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
    return max_length

answer = 1
for i in range(N): # 행
    for j in range(N - 1): # 열
        # 오른쪽이 다른 경우
        if j + 1 < N and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

            # 최대길이 검사
            answer = max(answer, check_length())

            # 원상복귀
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        # 밑쪽이 다른 경우
        if i + 1 < N and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            
            # 최대길이 검사
            answer = max(answer, check_length())

            # 원상복귀
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(answer)