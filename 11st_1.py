N = int(input())
max = 0

def convert(N,i):
    num = "0123456789ABCDEF"
    q,r = divmod(N,i)
    if q == 0:
        return num[r]
    else:
        return convert(q,i) + num[r]

for i in range(2,10):
    temp = convert(N,i)
    number = 1
    if "0" in temp:
        continue
    else:
        print(temp)
        for j in temp:
            j = int(j)
            number = number*j
    if number >= max:
        max = number
        idx = i

print([idx,max])