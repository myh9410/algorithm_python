import math

N = int(input())
num = math.factorial(N)
checker = True
if N <4:
    ans = num
else:
    while checker == True:
        if num < 10:
            break
        else:
            ans = 0
            for i in str(num):
                ans = ans + int(i)
                num = ans

print(ans)
