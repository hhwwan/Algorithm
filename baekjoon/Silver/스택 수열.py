"""
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.
"""

import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
stack = []
arr = []
result = True

for i in range(n):
    num = int(input())
    # 스택안에 아무것도 없거나 입력한 수보다 stack의 가장 마지막 숫자가 작을경우 스택에 삽입
    while not stack or stack[-1] < num:
        stack.append(cnt)
        cnt += 1
        arr.append('+')
    # 스택이 있고, 스택의 마지막 수가 현재 수와 동일하면 추출
    if stack and stack[-1] == num:
        stack.pop()
        arr.append('-')
    # stack의 마지막 수가 현재 수와 다른경우(더 커서 불가능)
    else:
        result = False
        break

if result:
    for i in arr:
        print(i)
else:
    print('NO')