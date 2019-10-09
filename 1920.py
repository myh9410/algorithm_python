N = int(input())
N_arr = list(map(int,input().split()))
M = int(input())
M_arr = list(map(int,input().split()))

N_arr.sort()
M_arr.sort()
min = 0
max = N-1
mid = (min + max)//2
while True:
    if len(M_arr) == 0:
        break
    if M_arr[0] < N_arr[min] or M_arr[0] > N_arr[max]:
        print(0)
        del M_arr[0]
    elif M_arr[0] == N_arr[min] or M_arr[0] == N_arr[max]:
        print(1)
        del M_arr[0]
    else:
        if M_arr[0] < N_arr[mid]:
            max = mid-1
        elif M_arr[0] > N_arr[mid]:
            min = mid+1
        else:
            print(1)
            del M_arr[0]

"""
import bisect
n = int(input())
a = sorted(map(int,input().split()))
m = int(input())
find = map(int,input().split())
for i in range(m):
    r = bisect.bisect(a,find[i])
    if a[r-1]!=find[i]:
        print(0)
    else: print(1)
"""

"""
n=input()
num = set(map(int,raw_input().split()))
m=input()
for i in map(int,raw_input().split()):
    if i in num:
        print 1
    else: print 0
"""