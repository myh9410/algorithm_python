def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    lcm = a*b//gcd(a,b)
    print(lcm)