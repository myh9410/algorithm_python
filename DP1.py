arr = [0,1]
n = int(input())
for i in range(n):
    arr.append(arr[i] + arr[i+1])

print(arr[n])