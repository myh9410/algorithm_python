import math

N = int(input())
l = list(map(int,input().split()))
count = 0
for i in l:
    if i < 2:
        pass
    else:
        temp = int(math.sqrt(i))+1
        ck = 1
        for j in range(2,temp):
            if i%j == 0:
                ck = 0
        if ck == 1:
            count+=1

print(count)