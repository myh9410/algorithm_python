def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
gcd = gcd(a,b)
lcm = a*b//gcd
print(gcd)
print(lcm)