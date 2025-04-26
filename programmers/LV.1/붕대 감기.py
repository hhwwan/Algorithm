"""
어떤 게임에는 붕대 감기라는 기술이 있습니다.

붕대 감기는 t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복합니다. 
t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복합니다. 
게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능합니다.

기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없습니다. 
몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용하며, 
연속 성공 시간이 0으로 초기화됩니다.

몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어듭니다. 
이때, 현재 체력이 0 이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없습니다.

당신은 붕대감기 기술의 정보, 캐릭터가 가진 최대 체력과 몬스터의 공격 패턴이 주어질 때 캐릭터가 끝까지 생존할 수 있는지 궁금합니다.

붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열 bandage와 최대 체력을 의미하는 정수 health, 
몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 attacks가 매개변수로 주어집니다. 
모든 공격이 끝난 직후 남은 체력을 return 하도록 solution 함수를 완성해 주세요. 
만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return 해주세요.
"""

def solution(bandage, health, attacks):
    sequence = 0
    monster = 0
    maximum = health
    for second in range(attacks[-1][0]+1):
        # 체력 회복을 했는데 최대 체력보다 높을 경우 최대체력으로 초기화
        if health > maximum:
            health = maximum
        # 몬스터 공격 시
        if second == attacks[monster][0]:
            health -= attacks[monster][1]
            sequence = 0 # 연속 회복 시간 초기화
            monster += 1
            if health <= 0: # 체력 0이하로 내려가면 -1 출력 후 종료
                return -1
        # 최대 체력보다 체력 작으면
        elif health < maximum:
            health += bandage[1] # 초당 체력 회복
            sequence += 1 # 연속 체력 회복 시간
            if sequence == bandage[0]: # 추가 회복량 시간 달성
                health += bandage[2]
                sequence = 0 # 연속 회복 시간 초기화
        
    return health