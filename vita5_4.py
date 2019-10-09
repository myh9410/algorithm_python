N = int(input())
ans = 0
temp = (N*(N+1)//2) % 1000000007
ans += temp*temp % 1000000007

print(ans)