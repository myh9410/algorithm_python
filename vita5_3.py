T = int(input())
dict = {'b': 'd','i':'i','l':'l','m':'m','n':'n','o':'o','p':'q','s':'z','u':'u','v':'v','w':'w','x':'x','d':'b','q':'p','z':'s'}
for _ in range(T):
    word = input()
    checker = True
    if len(word)%2 == 0: #짝
        temp = word[:len(word)//2]
        comp = word[(len(word)//2):]
        comp = comp[::-1]
    else:
        temp = word[:len(word)//2]
        comp = word[(len(word)//2)+1:]
        comp = comp[::-1]
    for i in range(len(temp)):
        if temp[i] not in dict:
            checker = False
        else:
            if dict[temp[i]] != comp[i]:
                checker = False
    if checker:
        print("Mirror")
    else:
        print("Normal")


