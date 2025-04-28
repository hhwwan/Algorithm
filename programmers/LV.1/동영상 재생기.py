"""
당신은 동영상 재생기를 만들고 있습니다. 
당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 
각 기능이 수행하는 작업은 다음과 같습니다.

10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
동영상의 길이를 나타내는 문자열 video_len, 
기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 
오프닝 시작 시각을 나타내는 문자열 op_start, 
오프닝이 끝나는 시각을 나타내는 문자열 op_end, 
사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 
이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.
"""

# 문자를 분, 초로 변환
def minutes_seconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return minutes, seconds


def solution(video_len, pos, op_start, op_end, commands):      
    # 초기값 변환
    video_min, video_sec = minutes_seconds(video_len)
    pos_min, pos_sec = minutes_seconds(pos)
    op_start_min, op_start_sec = minutes_seconds(op_start)
    op_end_min, op_end_sec = minutes_seconds(op_end)
    
    for i in commands:
        # 현재 시간이 오프닝 구간 사이에 있으면 op_end로 현재 시간 변경
        if (op_start_min < pos_min < op_end_min) or \
        (pos_min == op_start_min and pos_min < op_end_min and op_start_sec <= pos_sec) or \
        (pos_min == op_end_min and pos_min > op_start_min and op_end_sec >= pos_sec) or \
        (pos_min == op_start_min and pos_min == op_end_min and (op_start_sec <= pos_sec <= op_end_sec)):
            pos_min, pos_sec = op_end_min, op_end_sec
        
        # commands 명령 실행
        if i == 'next':
            pos_sec += 10
            # 초가 60초 넘어가면 보정
            if pos_sec >= 60:
                pos_sec -= 60
                pos_min += 1
            # 비디오 시간 넘어가면 video_len으로 고정
            if pos_min > video_min or (pos_min == video_min and pos_sec > video_sec):
                pos_min, pos_sec = video_min, video_sec
        elif i == 'prev':
            pos_sec -= 10    
            # 초가 0초 밑으로 내려가면 보정
            if pos_sec < 0:
                pos_sec += 60
                pos_min -= 1
            # 분도 0초 밑으로 내려가면 '00:00' 고정
            if pos_min < 0:
                pos_min, pos_sec = 0, 0
    
    # 반복문 끝난 후 오프닝 사이에 있을 경우 op_end로 시간 변경
    if (op_start_min < pos_min < op_end_min) or \
    (pos_min == op_start_min and pos_min < op_end_min and op_start_sec <= pos_sec) or \
    (pos_min == op_end_min and pos_min > op_start_min and op_end_sec >= pos_sec) or \
    (pos_min == op_start_min and pos_min == op_end_min and (op_start_sec <= pos_sec <= op_end_sec)):
        pos_min, pos_sec = op_end_min, op_end_sec

    return f"{pos_min:02d}:{pos_sec:02d}"