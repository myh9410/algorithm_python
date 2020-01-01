import sys

N = map(int,sys.stdin.readline())
arr = list(map(int,input().split()))
count = 0
ans = []
for i in range(len(arr)):
    temp = arr.copy()
    temp.remove(temp[i])
    maxval = max(temp)
    temp.remove(maxval)
    if maxval == sum(temp):
        count+=1
        ans.append(i+1)

if count == 0:
    print(0)
else:
    print(count)
    for i in ans:
        print(i,end=" ")
