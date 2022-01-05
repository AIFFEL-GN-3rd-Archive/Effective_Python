import sys
input = sys.stdin.readline
N = int(input())


for _ in range(N):
    s = list(input().strip())
    sum = 0
    for j in s:
        if j =="(":
            sum += 1
        else: 
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print('YES')
    elif sum > 0:
        print('NO')