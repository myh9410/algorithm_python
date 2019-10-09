arr = [[1,0],[0,1]]
T = int(input())
tc = []
for i in range(T):
    N = int(input())
    tc.append(N)

max(tc)

for i in range(max(tc)):
    arr.append([arr[i][0]+arr[i+1][0],arr[i][1]+arr[i+1][1]])

for i in tc:
    print(arr[i][0],arr[i][1])