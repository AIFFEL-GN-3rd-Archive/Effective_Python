import re
import sys

text = sys.stdin.readline().split()[0]
bomb = sys.stdin.readline().split()[0]
# while re.findall(bomb, text):
#   text = re.sub(bomb, '', text)

# print(text if text else 'FRULA')
# 위 방법은 시간복잡도 n^2으로 시간초과


stack = []
bomb_list = [k for k in bomb]
for i in text:
  stack.append(i)
  if len(stack) >= len(bomb_list):
    if stack[-len(bomb_list):] == bomb_list:
      for _ in range(len(bomb_list)):
        stack.pop()

print(''.join(stack) if stack else 'FRULA')
