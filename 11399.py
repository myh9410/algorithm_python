N = int(input())
time = list(map(int,input().split()))
time.sort()
ans = 0
for i in range(len(time)):
    if i == 0:
        ans += time[i]
    else:
        time[i] = int(time[i-1])+int(time[i])
        ans += time[i]

print(ans)