import sys
N,M = map(int,sys.stdin.readline().split())
map = [[0] * N for _ in range(M)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0
answer = 0
for k in range(M):
    temp = sys.stdin.readline()
    for l in range(N):
        map[k][l] = temp[l]

for i in range(M):
    for j in range(N):
        if map[i][j] == '#':
            count+=1
            ans = []
            ans.append([i,j])
            map[i][j] = '.'
            area = 1
            while ans != []:
                x = ans[0][0]
                y = ans[0][1]
                ans.remove(ans[0])
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N or map[nx][ny] == '.':
                        continue
                    map[nx][ny] = '.'
                    ans.append([nx,ny])
                    area+=1
            answer = max(answer, area)

for i in range(len(map)):
    count+= (map[i].count('#'))

print(count,answer,sep="\n")

