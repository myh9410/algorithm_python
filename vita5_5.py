N,T = map(int,input().split())
ans = 0
early = 1000000
for i in range(1,N+1):
    s,d = map(int,input().split())
    if s>=T:
        now = s
    else:
        now = (T-s+d-1) // d*d+s
    if early > now:
        early = now
        ans = i

print(ans)