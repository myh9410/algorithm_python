#E,S,M에 대해 몇년인지 구하는 문제
#15 x 28 x 19 개가 총 경우의 수 = 7980개
#걍 다해봐도 됨
# year mod 15 == E 이런식으로 풀어도 됨 (중국인의 나머지 정리)

E,S,M = map(int,input().split())


# 중국인의 나머지 정리
for i in range(1,7981):
    if i%15 == E and i%28 == S and i%19 == M:
        print(i)
    elif i%15 == 0 and i%28 == 0 and i%19 == 0:
        print(i)


"""
E,S,M = map(int,input().split())

e = 1
s = 1
m = 1

for i in range(1,7981):
    if e == E and s == S and m == M:
        print(i)
    e+=1
    s+=1
    m+=1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
"""