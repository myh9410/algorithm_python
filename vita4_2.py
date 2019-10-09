N = int(input())
s1 = set(map(int,input().split()))
M = int(input())
s2 = list(map(int,input().split()))
ans = []
for x in s2:
    if x in s1:
        print(1)
    else:
        print(0)