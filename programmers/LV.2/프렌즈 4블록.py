"""
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 
이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 
같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
"""

def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board] 
    
    while True:
        remove = set() # 제거 할 집합
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == 0:
                    continue
                if block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove.update({(i,j),(i,j+1),(i+1,j),(i+1,j+1)}) # 제거 좌표
        # 제거 할 집합이 더 이상 없다면 중단
        if not remove:
            break
        
        answer += len(remove)
        
        # 제거 한 좌표 위치 0으로 변경
        for i, j in remove:
            board[i][j] = 0
        
        for j in range(n):
            stack = [board[i][j] for i in range(m) if board[i][j] != 0]
            for i in range(m-1, -1, -1):
                board[i][j] = stack.pop() if stack else 0
                
    return answer