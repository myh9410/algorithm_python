def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

t = int(input())
for _ in range(t):
    temp = list(map(int,input().split()))
    sum = 0
    a = temp[1]
    for i in range(1,len(temp)):
        for j in range(1,i+1):
            if i == j:
                pass
            else:
                sum += gcd(temp[j],temp[i])
    print(sum)
