"""
선분 3개가 평행하게 놓여 있습니다. 
세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 
형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
"""
##### 못 풀었음

# 배열 사용
def solution(lines):
    answer = 0

    # 수직선 201개 표시 1차원 배열
    line_arr = [0] * 201

    # lines 순회
    for s, e in lines:

        # 음수를 없애기 위한 100씩 추가하기.
        s = s + 100
        e = e + 100

        # 배열의 표식을 위한 s ~ e - 1 범위까지 순회
        # 마지막을 포함하지 않는 이유는 경계선에 대한 중복 체킹을 방지하기 위함.
        for i in range(s, e):

            # 이미 한 번은 확인 되었으면, 정답 추가
            # 삼 중 이상 중첩을 막기 위해 조건문을 1로 제한..!
            if line_arr[i] == 1:
                answer += 1

            # 선분 체킹
            line_arr[i] += 1

    return answer


# Greedy 사용
def solution(lines):
    answer = 0

    # 시작 시점을 기준으로 오름차순 정렬
    lines.sort(key = lambda x : x[0])

    # 이전에 대한 선분 시작/종료 값
    prev_start = lines[0][0]
    prev_end = lines[0][1]

    for i in range(1, 3):

        # 현재 선분 가져오기
        line = lines[i]

        # 이전 시작과, 현재의 시작 중에 큰 부분 선택
        now_start = max(prev_start, line[0])

        # 이전 끝과, 현재의 끝 중에 작은 부분 선택
        now_end = min(prev_end, line[1])

        # 겹치는 범위가 존재한다면
        if now_start < now_end:

            # 겹치는 길이 만큼 정답에 추가
            answer += now_end - now_start

            # 이전 시작값을, 현재의 끝으로 지정하여 이미 산정된 과거의 겹치는 선분을 계산하지 못하도록 제한!
            prev_start = now_end

            # 이전 끝 값을, 가장 큰 end 값으로 선정함. 현재 조사하고 있는 선분 중에서 가장 큰 end로 선정해야 다음 선분과 겹치는 부분을 더 많이 겹치는 방향으로 비교할 수 있음.
            prev_end = max(prev_end, line[1])
        else:

            # 겹치는 구간이 없으므로 신규로 다시 지정
            prev_start = line[0]
            prev_end = line[1]

    return answer