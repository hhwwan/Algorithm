"""
한 줄로 된 간단한 에디터를 구현하려고 한다. 
이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 
문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.

L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함

초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
"""

# 내 풀이 -> 시간초과
import sys
input = sys.stdin.readline

word = list(input())
N = len(word) - 1 # 리스트로 받으면 맨 뒤에 '\n' 자동삽입되므로 -1
M = int(input())

for i in range(M):
    command = input().split()
    if command[0] == 'L': 
        if N > 0 :
            N -= 1
    elif command[0] == 'D':
        if N < len(word) - 1:
            N += 1
    elif command[0] == 'B':
        if word and N > 0:
            del word[N-1] # 커서 왼쪽에 있는 문자 삭제 후 커서도 한칸 앞으로
            N -= 1
    elif command[0] == 'P':
        word.insert(N, command[1]) # 커서 왼쪽에 문자 삽입 후 커서 한칸 뒤로
        N += 1
print(''.join(word))

# 답안
import sys
input = sys.stdin.readline

left_stack = list(input().rstrip())  # 초기 문자열의 문자들을 왼쪽 스택에 넣는다
right_stack = []

M = int(input())
for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])

# 최종 문자열은 왼쪽 스택 + 오른쪽 스택(뒤집어서)
print(''.join(left_stack + right_stack[::-1]))
