N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
ans = 0
count = 1
"""
for i in range(len(arr)):
    if i <len(arr)-1:
        s = arr[i]
        temp = s
        if s == M:
            ans+=1
        for j in range(i+1,len(arr)):
            e = arr[j]
            temp +=e
            if temp < M:
                continue
            elif temp == M:
                ans +=1
                break
            else:
                break
    elif i == len(arr):
        break
"""
#위에처럼 이중for문 안쓰고 이렇게 해결 가능
s = 0
e = 0
sum = 0
cnt = 0
while s < N:
    if e < N and sum < M:
        sum += arr[e]
        e += 1
    else:
        sum -= arr[s]
        s += 1
    if sum == M:
        cnt += 1

print(cnt)

# M보다 작으면 e를 늘리고
# M보다 크면 s를 늘리고 해서 다시 풀어보자
# while문써서 s,e값 변경해주고 e가 len(arr)이랑 같아지면 종료?

# 시간복잡도 O(N)
