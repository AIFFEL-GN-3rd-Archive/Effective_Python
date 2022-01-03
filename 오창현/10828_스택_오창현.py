import sys
n = int(sys.stdin.readline())

global stack
stack = []
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


for _ in range(n):
    do = sys.stdin.readline()
    do = do.split()

    if do[0] == "push":
        push(do[1])
    else:
        dodo = do[0]+"()"
        eval(dodo)
