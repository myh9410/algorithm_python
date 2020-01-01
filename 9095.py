#N중 for문
#10중 for문
#3^n의 시간복잡도
T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    for a in range(1,4):
        if a ==n:
            count+=1
        for b in range(1, 4):
            if a+b == n:
                count += 1
            for c in range(1, 4):
                if a+b+c == n:
                    count += 1
                for d in range(1, 4):
                    if a+b+c+d == n:
                        count += 1
                    for e in range(1, 4):
                        if a+b+c+d+e == n:
                            count += 1
                        for f in range(1, 4):
                            if a+b+c+d+e+f == n:
                                count += 1
                            for g in range(1, 4):
                                if a+b+c+d+e+f+g == n:
                                    count += 1
                                for h in range(1, 4):
                                    if a+b+c+d+e+f+g+h == n:
                                        count += 1
                                    for i in range(1, 4):
                                        if a+b+c+d+e+f+g+h+i == n:
                                            count += 1
                                        for j in range(1, 4):
                                            if a+b+c+d+e+f+g+h+i+j == n:
                                                count+=1
    print(count)