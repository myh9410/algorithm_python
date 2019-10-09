#Sweeping Algorithm
N,L = map(int,input().split())
dig = [0 for _ in range(L+2)]
H = [0 for _ in range(L+2)]
temp = list(map(int,input().split()))
H[1] = temp[0]
for i in range(len(temp)):
    H[i+1] = temp[i]

print(H)
for _ in range(N):
    S,E,D = map(int,input().split())
    dig[S] += D
    dig[E+1] -= D

mn = 987654321
mx = -987654321

for i in range(1,L+1):
    dig[i] += dig[i-1]
    H[i] -= dig[i]
    mx = max(mx, H[i])
    mn = min(mn, H[i])

print(mx,mn,sep="\n")