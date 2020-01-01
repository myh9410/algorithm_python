"""
import math
ck = True
mx2 = 0
while ck is True:
    p=-1
    q=-1
    n = int(input())
    if n == 0:
        ck = False
    mxval = int(math.sqrt(n))+1
    pm = [x for x in range(2, n + 1)]
    for i in range(2,mxval+1):
        for j in pm:
            if j == 2 or j == 3 or j==5 or j==7:
                pass
            else:
                if j%i == 0:
                    pm.remove(j)
    print(pm)
    for k in pm:
        if k%2 == 0:
            pass
        else:
            if n-k in pm:
                mx = abs(n-k-k)
                if mx > mx2:
                    mx2 = mx
                    p = k
                    q = n - k
    if p!= -1 and q != -1:
        print(n, " = ", p, " + ", q)
    else:
        print("Goldbach's conjecture is wrong.")
"""
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i
prime = prime[1:]
while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False:
            print("{0} = {1} + {2}".format(n, p, n-p))
            break