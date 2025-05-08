"""
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.
"""

import sys
input = sys.stdin.readline

S = input().rstrip()
answer = []
result = ''
temp = False

for word in S:
    if word == '<':
        # '<' 전에 있던 문자들 뒤집고 answer에 추가 후 '<' 추가
        if result:
            answer.append(result[::-1])
            result = ''
        temp = True # '<','>' 사이라는것 표시
        answer.append(word)
    # '>' 그대로 answer에 추가
    elif word == '>':
        temp = False #'<','>' 끝났다고 표기
        answer.append(word)
    # '<','>' 사이에 있는 문자들은 그대로 answer에 추가
    elif temp:
        answer.append(word)
    # 공백 나오면 지금까지 저장된 문자열 뒤집어서 answer에 추가
    elif word == ' ':
        answer.append(result[::-1])
        answer.append(' ')
        result = ''
    # '<','>' 사이가 아닌 그냥 문자는 일단 저장
    else:
        result += word

if result:
    answer.append(result[::-1])

print(''.join(answer))