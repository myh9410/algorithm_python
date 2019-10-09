
n = 3
arr = [0]
computers = [[1,1,0],[1,1,0],[0,0,1]]
"""
for i in range(len(computers)):
    computers[i][i] = 0

print(computers)
for i in computers:
    for j,k in zip(i,range(len(i))):
        if j == 1 and k not in arr:
            arr.append(k)

if len(arr) == n:
    print(1)
else:
    print(1+n-len(arr))

"""
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    print(temp)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                print(i,j,temp)
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))

print(solution(n,computers))
