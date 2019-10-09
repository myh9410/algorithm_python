arr = []
N,M = map(int,input().split())
str = input()
str += "$"

i=0

while i < (len(str)):
    if arr == []:
        arr.append([str[i],1])
    elif arr[-1][0] == str[i]:
        arr[-1][1] += 1
    else:
        if arr[-1][1] >= M:
            arr.pop()
            i-=1
        else:
            arr.append([str[i], 1])
    i+=1

print(arr)
arr.pop()
ans = ""
if arr == []:
    print("CLEAR!")
else:
    for i in range(len(arr)):
        ans += arr[i][0]
    print(ans)

