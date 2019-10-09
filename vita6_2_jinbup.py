N,T = map(str,input().split())
N = int(N)

for i in range(2,17):
    sum=0
    for j in range(len(T)):
        val = ord(T[j]) - ord('A')+10 if ord(T[j]) >= ord('A') else ord(T[j])-ord('0')
        if val >=i:
            break
        sum*=i
        sum+=val
    if j == len(T)-1 and sum == N:
        print(i)
        break
