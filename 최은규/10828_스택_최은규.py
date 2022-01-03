import sys

def push(i):
  stack.append(int(i))

def pop():
  if stack:
    print(stack.pop())
  else:
    print(-1)

def size():
  print(len(stack))

def empty():
  if stack:
    print(0)
  else:
    print(1)

def top():
  if stack:
    print(stack[-1])
  else:
    print(-1)

def main():

  N = int(sys.stdin.readline())
  global stack
  stack = []
  
  for i in range(N):
    com = sys.stdin.readline()
    com = com.split()
    if com[0] == 'push':
      push(com[1])
    elif com[0] == 'pop':
      pop()
    elif com[0] == 'size':
      size()
    elif com[0] == 'empty':
      empty()
    else:
      top()
    

if __name__ == '__main__':
  main()