#n명중에 i번째, j번째를 제외한 n-2명 키의 합을 구함
#sum에 모든 9명 키 저장 후, i번째 j번째 값만 빼줌. 그게 100이면 종료
tall = []
for i in range(9):
    h = int(input())
    tall.append(h)

for i in range(len(tall)):
    for j in range(i):
        temp = tall[:]
        temp.remove(temp[i])
        temp.remove(temp[j])
        if sum(temp) == 100:
            ans = temp

ans.sort()
for i in ans:
    print(i)