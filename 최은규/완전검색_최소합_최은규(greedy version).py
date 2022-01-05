import sys
import itertools
import copy

N = int(sys.stdin.readline())
df = []
li = []
for k in range(N):
    arr = sys.stdin.readline().split()
    df.append([int(n) for n in arr])
    li.append(k)

i = 0
j = 0
result = 0
while i <= N-1 and j <= len(df[0])-1:
    result += df[i][j]
    try:
        if df[i+1][j] < df[i][j+1]:
            i += 1
        else:
            j += 1
    except:
        if i == N-1:
            j += 1
        elif j == len(df[0])-1:
            i += 1
        else:
            break
print(result)

