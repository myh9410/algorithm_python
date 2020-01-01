#테트로미노
#NxM 크기의 종이 위에 테트로미노를 하나 놓아서
#놓인 칸에 쓰여있는 수의 합을 최대로 하는 문제
# 4<= N,M <=500
# ㅁㅁㅁㅁ > N(M-3)개 (2가지)           ㅁ      > 4가지       ㅁㅁㅁ >4가지   ㅁㅁ >1가지
# ㅁ                                   ㅁㅁ                    ㅁ           ㅁㅁ
# ㅁ                                     ㅁ
# ㅁㅁ > (N-2)(M-1) (8가지) 등 최대 NXM보다는 항상 적게 들어갈 수 밖에 없음
# 블럭 회전까지 생각했을 때 총 블럭 종류 수 19개
#총 경우의 수 19 X NM > 최대로 해봐야 약 5백만개 (많지 않으므로 다 해보면 됨)
#소스1 - if문 다 돌려서 19가지 블록에 대해 코드 짤수도 있음
#소스2 - 행렬로 블록 만들어서 할수도 있음





"""
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
 for j in range(m):
 if j+3 < m:
 temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
 if ans < temp: ans = temp

 if i+3 < n:
 temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
 if ans < temp: ans = temp

 if i+1 < n and j+2 < m:
 temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
 if ans < temp: ans = temp

 if i+2 < n and j+1 < m:
 temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
 if ans < temp: ans = temp

 if i+1 < n and j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
 if ans < temp: ans = temp

 if i+2 < n and j-1 >= 0:
 temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
 if ans < temp: ans = temp

 if i-1 >= 0 and j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
 if ans < temp: ans = temp

 if i+2 < n and j+1 < m:
 temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
 if ans < temp: ans = temp

 if i+1 < n and j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
 if ans < temp: ans = temp

 if i+2 < n and j+1 < m:
 temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
 if ans < temp: ans = temp

 if i+1 < n and j+1 < m:
 temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
 if ans < temp: ans = temp

 if i-1 >= 0 and j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
 if ans < temp: ans = temp

 if i+2 < n and j+1 < m:
 temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
 if ans < temp: ans = temp

 if i+1 < n and j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
 if ans < temp: ans = temp

 if i+2 < n and j-1 >= 0:
 temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
 if ans < temp: ans = temp

 if j+2 < m:
 temp = a[i][j] + a[i][j+1] + a[i][j+2]
 if i-1 >= 0:
 temp2 = temp + a[i-1][j+1]
 if ans < temp2: ans = temp2

 if i+1 < n:
 temp2 = temp + a[i+1][j+1]
 if ans < temp2: ans = temp2


 if i+2 < n:
 temp = a[i][j] + a[i+1][j] + a[i+2][j]
 if j+1 < m:
 temp2 = temp + a[i+1][j+1]
 if ans < temp2: ans = temp2

 if j-1 >= 0:
 temp2 = temp + a[i+1][j-1]
 if ans < temp2: ans = temp2

print(ans)

"""