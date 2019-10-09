N = int(input())
arr = []
arr2 = []

for i in range(N):
    s, e = map(str, input().split())
    s1, s2 = s.split("/")
    e1, e2 = e.split("/")
    start = int(s1)*100 + int(s2)
    end = int(e1) * 100 + int(e2)
    arr.append([start,end])

for i in arr:
    arr2.append(i[0])
    arr2.append(i[1])

arr2.sort()

count = 0
for i,j in zip(arr2,reversed(arr2)):
    if count == len(arr2)//2:
        break
    else:
        if [i,j] in arr:
            answer = "Yes"
            arr.remove([i,j])
        else:
            answer = "No"
            break
    count+=1

print(answer)
