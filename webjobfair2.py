bishops = ["D5","E8","G2"]
horarr = ["A","B","C","D","E","F","G","H"]
ans = []
for i in bishops:
    hor = i[0]
    ver = int(i[1])
    cur = horarr.index(hor)
    for j in range(0,cur):
        temp = cur-horarr.index(horarr[j])
        if 0 <= ver + temp <= 8:
            ans.append([j, ver + temp])
        if 0 <= ver - temp <= 8:
            ans.append([j, ver - temp])
        else:
            pass
    for k in range(cur+1,len(horarr)):
        temp = cur - horarr.index(horarr[k])
        if 0<=ver+temp<=8:
            ans.append([k, ver + temp])
        if 0<=ver-temp<=8:
            ans.append([k, ver - temp])
        else:
            pass

ans.append([cur,ver])
ans = list(set([tuple(item) for item in ans]))
print(ans)
print(64 - len(ans))
