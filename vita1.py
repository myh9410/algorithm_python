N = int(input())
arr = []
for i in range(N):
    ans = ""
    line = input()
    for i in range(len(line)):
        if "a" in line[i] or "A" in line[i] or "e" in line[i] or "E" in line[i] or "i" in line[i] or "I" in line[i] or "o" in line[i] or "O" in line[i] or "u" in line[i] or "U" in line[i]:
            ans += line[i]
    if ans == "":
        ans += "???"

    arr.append(ans)

for i in range(len(arr)):
    print(arr[i])