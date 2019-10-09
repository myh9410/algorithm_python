import sys

m,n = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
sum = [None]*len(arr)
sum[0] = arr[0]
for i in range(1,len(arr)):
    sum[i] = sum[i-1] + arr[i]

for _ in range(n):
    s,e = map(int, input().split())
    if s==1:
        print('{0:+d}'.format(sum[e-1]))
    else:
        print('{0:+d}'.format(sum[e-1]-sum[s-2]))
