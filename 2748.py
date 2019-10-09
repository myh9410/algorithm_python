n = int(input())

t1 = 0
t2 = 1

for i in range(0,n):
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print(t1)
