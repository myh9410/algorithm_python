N = int(input())
arr = []
count = 0
for _ in range(2*N):
    temp = input()
    if "add" in temp:
        a,b = temp.split()
        arr.append(b)
    #else:
        # if len(arr) != 0 and arr[0] ==

print(count)