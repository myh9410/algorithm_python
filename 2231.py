#TC계속 틀림
N = int(input())
br = False
answer = 0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if 101*int(i)+11*int(j)+2*int(k) == N:
                if answer != 0:
                    break
                else:
                    answer = 100*int(i)+10*int(j)+1*int(k)
            elif 101*int(i)+11*int(j)+2*int(k) > N:
                br = True
                break
        if br == True:
            break
    if br == True:
        break
print(answer)