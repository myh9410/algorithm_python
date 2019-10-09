import sys
R, C, K = map(int, sys.stdin.readline().split())
data = [[0] * C for _ in range(R)]
for i in range(R):
    temp = sys.stdin.readline()
    for j in range(C):
        data[i][j] = int(temp[j])

visit = [[0] * C for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit[0][0] = 1