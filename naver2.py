import math
n = int(input())
s1 = set()
for i in range(n+1,1,-1):
    f_i = math.factorial(i)
    if i-2 <= 1:
        s1.add(f_i)
    else:
        for j in range(i-2,1,-1):
            j_i = math.factorial(j)
            temp = f_i//j_i
            if f_i < 1000000000000:
                s1.add(f_i)
            if temp > 100000000000:
                break
            else:
                s1.add(temp)

ans = list(s1)
ans.sort()
print(ans[n-1])
