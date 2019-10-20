L = int(input())
arr = list(map(int,input().split()))
K = 100000
ans = -1

for i in range(1,101):
    st = 0
    ed = -1
    for j in range(0,L):
        if arr[j] == i:
            st = max(st,j-ed)
            ed = j
    st = max(st,L-ed)
    if K >= st:
        K = st
        ans = i

print(ans,K)