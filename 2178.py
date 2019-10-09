#2차원 배열, 미로탐색 - BFS
import sys
def main():
    x, y = map(int, sys.stdin.readline().split())
    data = [[0] * y for _ in range(x)]
    for i in range(x):
        temp = sys.stdin.readline()
        for j in range(y):
            data[i][j] = int(temp[j])
    print("data")
    print(data)
    visit = [[0] * y for _ in range(x)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # bfs
    arr = []
    arr.append((0, 0))
    visit[0][0] = 1
    while arr:
        a, b = arr.pop(0)
        if a == x - 1 and b == y - 1: #리스트의 max일때
            print(visit[a][b]) #visit리스트에서 제일 마지막 값 출력
            sys.exit()
        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            print(a, b)
            print(ax, ay)
            print(visit)
            if ax >= 0 and ax < x and ay >= 0 and ay < y:
                if visit[ax][ay] == 0 and data[ax][ay] == 1:
                    visit[ax][ay] = visit[a][b] + 1
                    arr.append((ax, ay))

if __name__ == '__main__':
    main()

"""
def dfs(y, x, depth):
    if x <0 or y <0 or y >= Nor x >= M:#영역초과
        return
 
    if y== N-1 and x== M-1:#도착
        global Min
        if depth <Min:
            Min = depth
        return
 
    for iin range(4):
        wX= x+ dir[i][0]
        wY= y+ dir[i][1]
        if wX <0 or wY <0 or wY >= Nor wX >= M: # 영역초과
            pass
        elif visit[wY][wX]== 0 and map[wY][wX]== '1':
            visit[wY][wX]= 1
            dfs(wY, wX, depth+1)
            visit[wY][wX]= 0
 
 
N, M= map(int,input().split())
map = [""]* N
visit= [[0]* Mfor _in range(N)]
dir = [[0,1], [1,0], [0,-1], [-1,0]]
 
Min = N*M
 
for iin range(N):
    map[i]= input()
 
dfs(0,0,1)
print(Min)


출처: https://tkql.tistory.com/24 [싸비]
"""