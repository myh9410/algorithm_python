N,K = input().split()
arr = []
count = 0

for i in range(0,int(N)):
    num = int(input())
    arr.append(num)

arr.reverse()
temp = int(K)
while(True):
    if len(arr) == 0:
        break

    if temp < arr[0]:
        arr.remove(arr[0])
    else:
        count += temp//arr[0]
        temp = temp - (temp//arr[0])*arr[0]
        arr.remove(arr[0])

print(count)