#다람쥐와 도토리
#start = (0,0)
#end = (N,M)
#dotori = (d1,d2)
#trap = (t1,t2)
N,M = map(int,input().split())
d1,d2 = map(int,input().split())
t1,t2 = map(int,input().split())

matrix = [[0]*(N+1) for i in range(M+1)]
print(matrix)