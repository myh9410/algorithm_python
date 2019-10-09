N = int(input())
tree = list(map(int,input().split()))
s = 0
e = N-1
si = 0
se = 0
ans = 0
while s<e:
    placard = min(tree[s], tree[e])*(e-s)
    if ans < placard:
        ans = placard
        si = s+1
        se = e+1
    if tree[s] < tree[e]:
        s+=1
    else:
        e-=1

print(ans)
print(si,se)
