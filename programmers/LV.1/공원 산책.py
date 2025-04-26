"""
지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 
산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

["방향 거리", "방향 거리" … ]
예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 
로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 
로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

# 내가 푼 것
def solution(park, routes):
    answer = []
    move = {'E': [0,1],
            'W': [0,-1],
            'S': [1,0],
            'N': [-1,0]
        } # 동,서,남,북 순
    
    # 시작 지점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start_x = i
                start_y = j
                break

    # 방향 찾아서 이동       
    for i in routes:
        mv_route = i.split()
        nx = start_x
        ny = start_y
        for j in range(int(mv_route[1])):
            start_x += move[mv_route[0]][0]
            start_y += move[mv_route[0]][1]
            # 범위 안 벗어나는지 체크
            if start_x >= 0 and start_x < len(park) and start_y >= 0 and start_y < len(park[0]):
                # 벽 만나면 패스
                if park[start_x][start_y] == 'X':
                    start_x = nx
                    start_y = ny
                    break
            # 범위 벗어나면 패스
            else:
                start_x = nx
                start_y = ny
                break
        answer = [start_x,start_y]
            
    return answer

# Chatgpt가 가독성 좋게 수정해준 것
def solution(park, routes):
    answer = []
    
    move = {
        'E': [0, 1],
        'W': [0, -1],
        'S': [1, 0],
        'N': [-1, 0]
    }  # 동, 서, 남, 북 방향
    
    # 시작 지점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start_x = i
                start_y = j
                break
                
    # 명령 수행
    for i in routes:
        direction, distance = i.split()
        distance = int(distance)
        
        nx = start_x
        ny = start_y
        
        valid = True  # 이동 가능한지 체크
        
        for _ in range(distance):
            nx += move[direction][0]
            ny += move[direction][1]
            
            # 공원 범위 체크
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                valid = False
                break
            
            # 장애물 체크
            if park[nx][ny] == 'X':
                valid = False
                break
        
        # 이동 가능하면 업데이트
        if valid:
            start_x = nx
            start_y = ny
            
    answer = [start_x, start_y]
    return answer
