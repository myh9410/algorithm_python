# 정수 삼각형
# 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
N = int(input())
triangle = [list(map(int,input().split())) for _ in range(N)]

print(triangle)
# 총 N - 1번의 계산이 이루어진다.
for i in range(N - 1):
    for j in range(len(triangle[i + 1])):
        # 첫번쨰와 끝부분 같은 경우는 그냥 더해주면 된다.
        if(j == 0):
            triangle[i + 1][j] = triangle[i][j] + triangle[i + 1][j]
        elif(j == len(triangle[i + 1]) - 1):
            print(j)
            triangle[i + 1][-1] = triangle[i][-1] + triangle[i + 1][-1]
            print(triangle)
        # 그렇지 않고 중간에 있는 숫자들(예를 들어 1 3 1 의 3같은 경우)은 바로 위 그룹의
        # 자기 자신의 인덱스 - 1 과 자기 자신의 인덱스와의 합이 총 2개가 나오는데
        # 2개 중 max를 고려하여 교체해야한다.
        else:
            triangle[i + 1][j] = max(triangle[i][j - 1] + triangle[i + 1][j], triangle[i][j] + triangle[i + 1][j])

print(max(triangle[-1]))