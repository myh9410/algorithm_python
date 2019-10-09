ans = ""
def divide(str):
    count = 0
    if str == "":
        return ""
    else:
        for i in range(len(str)):
            if str[i] == "(":
                count +=1
            else:
                count -=1
            if count == 0:
                if i+1 == len(str):
                    u = str[:i+1]
                    v = ""
                else:
                    u = str[:i+1]
                    v = str[i+1:]
                break
        return u,v

def checker(str):
    for i in range(len(str)):
        if i == 0:
            if str[i] == "(":
                return True
            else:
                return False



p = input()
u,v = divide(p)
boo = True

while boo is True:
    if len(ans) == len(p):
        boo = False
        break
    if checker(u) is True:
        ans += u
        if v == "" or v == "()":
            ans +=v
        else:
            u,v = divide(v)
    else:
        if v == "" or v == "()":
            u = u[1:-1].replace("(","+").replace(")","-")
            u = u.replace("+",")").replace("-","(")
            ans = ans + "(" + v + ")" + u
        else:
            u, v = divide(v)

print(ans)



