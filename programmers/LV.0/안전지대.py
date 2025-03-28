"""
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 
지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 
안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
"""

def solution(board):
    answer = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                if x-1 >= 0 and board[x-1][y] == 0:
                    board[x-1][y] = 2
                if x+1 < len(board) and board[x+1][y] == 0:
                    board[x+1][y] = 2
                if y-1 >= 0 and board[x][y-1] == 0:
                    board[x][y-1] = 2
                if y+1 < len(board) and board[x][y+1] == 0:
                    board[x][y+1] = 2
                if x-1 >= 0 and y-1 >= 0 and board[x-1][y-1] == 0:
                    board[x-1][y-1] = 2
                if x-1 >= 0 and y+1 < len(board) and board[x-1][y+1] == 0:
                    board[x-1][y+1] = 2
                if x+1 < len(board) and y-1 >= 0 and board[x+1][y-1] == 0:
                    board[x+1][y-1] = 2
                if x+1 < len(board) and y+1 < len(board) and board[x+1][y+1] == 0:
                    board[x+1][y+1] = 2

    for x in range(len(board)):
        for yy in range(len(board)):
            if board[x][yy] == 0:
                answer += 1
                yy += 1
            else:
                yy += 1
    print(board)
    return answer