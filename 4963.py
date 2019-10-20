from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for a in range(8):
            i = v[0] + dx[a]
            j = v[1] + dy[a]
            if 0<=i<=h-1 and 0<=j<=w-1 and mapmap[i][j]:
                mapmap[i][j] = 0
                q.append([i, j])


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mapmap = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if mapmap[i][j]:
                count += 1
                bfs([i, j])
    print(count)
