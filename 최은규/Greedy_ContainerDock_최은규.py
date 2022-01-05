import sys

N = int(sys.stdin.readline())
start = []
end = []
for k in range(N):
    arr = sys.stdin.readline().split()
    start.append(int(arr[0]))
    end.append(int(arr[1]))


time = 0
result = 0
while True:
    print(start)
    print(end)
    res_list = list(filter(lambda x: start[x] == min(start), range(len(start))))
    if len(res_list) != 1:
        s_index = end.index(min([end[k] for k in res_list]))

    else:
        s_index = start.index(min(start))
    time = end[s_index]
    print(time)
    result += 1
    if time > max(start):
        break
    while min(start) < time:
        idx = start.index(min(start))
        start.pop(idx)
        end.pop(idx)


print('result :', result)
