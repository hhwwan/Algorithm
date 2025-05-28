"""
XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 
이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. 
"최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, 
"소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 
예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 
위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 
한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 
유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 
유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.
"""

# 내가 푼 코드 -> 한가지 방법만 탐색하므로 정답이 아닌 경우가 존재
def solution(k, dungeons):
    answer = 0
    sort_dungeons = sorted(dungeons, key=lambda x: (x[0]-x[1], x[0]), reverse=True)
    
    for i in sort_dungeons:
        if k < i[0]:
            continue
        else:
            k -= i[1]
            answer += 1
            
    return answer

# permutations 사용한 방법
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 가능한 모든 순서 생성 (permutations)
    for i in permutations(dungeons):
        now_stamina = k
        cnt = 0
        # 현재 체력이 더 높을때만 실행
        for min_stamina, use_stamina in i:
            if now_stamina >= min_stamina:
                now_stamina -= use_stamina
                cnt += 1
            else:
                break
        # 가장 높은거 선택
        if cnt >= answer:
            answer = cnt
            
    return answer