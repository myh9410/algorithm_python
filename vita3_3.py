N,M = map(int,input().split())
hor = int(N/20)*int(M/40)
ver = int(N/40)*int(M/20)
square = 2*int(N/40)*int(M/40)
ans = hor + ver - square

print(ans)