N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
arrA = [0 for i in range(100000)]
arrB = [0 for j in range(100000)]

for i in A:
    arrA[i-2] += 1
    arrA[i-1] += 1
    arrA[i] += 1
    arrA[i+1] += 1
    arrA[i+2] += 1

for j in B:
    arrB[j-2] += 1
    arrB[j-1] += 1
    arrB[j] += 1
    arrB[j+1] += 1
    arrB[j+2] += 1

print(arrA.index(max(arrA)), arrB.index(max(arrB)))
if arrA.index(max(arrA)) > arrB.index(max(arrB)):
    print("good")
else:
    print("bad")