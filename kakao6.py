s= input()

v = True
t = len(s)//2

while v is True:
    print(s.count(s[:t]))
    t = t//2
    print(t)
    if t == 2:
        v = False