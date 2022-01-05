# 3
# 1 2 3
# 2 3 4
# 3 4 5
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

#가로로 이동하는 부분에 대한 순열
count = N+len(df[0])-1
per = itertools.combinations_with_replacement(li, count - N)
# combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
result = []
for i in list(per):
    res = li.copy()
    res.extend(list(i))
    res = sorted(res)
    print(res)
    df_copy = copy.deepcopy(df)
    j = 0
    summ = 0
    for i, k in enumerate(res):
        summ += df_copy[k][j]
        try:
            if k == res[i+1]:
                j += 1
        except:
            break

    result.append(summ)
print(result)
print(min(result))