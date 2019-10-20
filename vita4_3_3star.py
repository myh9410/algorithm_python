#ccw - counter clock wise?
import sys
import math
N = int(sys.stdin.readline())
temp = math.atan2(1,1)
for i in range(N):
    a,b = map(float,sys.stdin.readline().split())
    if i <2:
        pass
    else:
        t1 = math.atan2(b,a)
        print(temp,t1,a,b)
        if t1 > temp:
            print("LEFT")
        else:
            print("RIGHT")
        temp = t1