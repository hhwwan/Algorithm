"""
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
1 2 3
4 5 6
7 8 9
* 0 #

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
"""

def solution(numbers, hand):
    answer = ''
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']] # 손에 맞춰서 키패드 지정
    L_point = [0,3] # keypad 좌표라 가정
    R_point = [2,3]
    
    for i in numbers:
        # 왼손으로 누를 때
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            L_point = [0, keypad[0].index(i)]
        # 오른손으로 누를 때
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            R_point = [2, keypad[2].index(i)]
        else:
            # 왼손 거리가 더 가까울 때
            if abs(keypad[1].index(i)-L_point[1]) + abs(1-L_point[0]) < abs(keypad[1].index(i)-R_point[1]) + abs(1-R_point[0]):
                answer += 'L'
                L_point = [1, keypad[1].index(i)]
            # 오른손 거리가 더 가까울 때
            elif abs(keypad[1].index(i)-L_point[1]) + abs(1-L_point[0]) > abs(keypad[1].index(i)-R_point[1]) + abs(1-R_point[0]):
                answer += 'R'
                R_point = [1, keypad[1].index(i)]
            # 거리가 같을 때
            else:
                if hand == 'left':
                    answer += 'L'
                    L_point = [1, keypad[1].index(i)]
                else:
                    answer += 'R'
                    R_point = [1, keypad[1].index(i)]
            
    return answer