a,b = map(int,input().split())
dict = {}
for i in range(a,b+1):
    count = dict.get(i, 0)
    dict[i] = count + 1
    temp = int(i/2)
    while temp >= 2:
        if i%temp == 0:
            count = dict.get(temp,0)
            dict[temp] = count + 1
        temp -= 1

print(dict)
print(max(dict, key=dict.get))


## 위의 방식은 시간초과가 남
# GREEDY ALGORITHM 사용
def leastOne(a):
    for i in range(2,int(a**0.5)):
        if a%i == 0:
            return i
    return a

a,b = map(int,input().split())
if a != b: #a와 b가 다를때는 2가 가장 많이 나옴
    print(2)
else:   #a와 b가 같을때는 2보다 이상의 가장 작은 약수
    print(leastOne(a))

