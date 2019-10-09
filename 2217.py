N = int(input())
arr = []
w=0
for i in range(0,N):
    rope = int(input())
    arr.append(rope)

arr.sort(reverse=True)

for i in range(len(arr)):
    if i == 0:
        temp = arr[i]*(i+1)
    else:
        temp2 = arr[i]*(i+1)
        if temp2 >= temp:
            temp = temp2

print(temp)