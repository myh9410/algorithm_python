#JMOS
N = int(input())
R = list(map(int,input().split()))
dp = [0]*len(R)

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if R[j] < R[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))