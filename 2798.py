N,M = map(int,input().split())# 입력받은 값들을 int형으로 변경시켜줌
card = list(map(int, input().split(' '))) #입력받은 값들을 int형으로 변경하여 list에 넣어줌
answer = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N): #조합, for문 3개를 이용하여 배열내에서 값 3개씩에 대한 탐색이 가능
            if (card[i]+card[j]+card[k]) <= M and M - (card[i]+card[j]+card[k]) < M - answer: # 제일 차이가 적은 카드 3장을 확인 가능
                answer = (card[i]+card[j]+card[k])
print(answer)




