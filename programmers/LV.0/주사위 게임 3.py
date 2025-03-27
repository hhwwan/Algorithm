"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""

from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice)

    # 모두 같은 숫자라면
    if len(counter) == 1:
        return 1111 * dice[0]
    elif len(counter) == 2:
        nums = list(counter.items()) # [(숫자, 개수)]
        # 3개 같고, 1개 다른 경우
        if nums[0][1] == 3:
            p = nums[0][0]
            q = nums[1][0]
            return (10 * p + q) ** 2
        elif nums[1][1] == 3:
            p = nums[1][0]
            q = nums[0][0]
            return (10 * p + q) ** 2
        # 2개, 2개인 경우
        elif nums[0][1] == 2:
            return (nums[0][0] + nums[1][0]) * abs(nums[0][0] - nums[1][0])
    # 2개는 같고, 1개, 1개
    elif len(counter) == 3:
        nums = list(counter.items()) # [(숫자, 개수)]
        another = []
        for i in nums:
            if i[1] == 1:
                another.append(i[0])
        return another[0] * another[1]
    # 다 다른 경우
    else:
        return min(dice)
        