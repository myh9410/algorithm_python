arr1 = []
arr2 = []
ans = 0
for i in range(3):
    a1,a2 = map(int,input().split())
    arr1.append(a1)
    arr2.append(a2)

ans += arr1[0]*arr2[1]+arr1[1]*arr2[2]+arr1[2]*arr2[0]
ans -= arr1[0]*arr2[2]+arr1[2]*arr2[1]+arr1[1]*arr2[0]
ans = ans/2
print('%0.2f' % round(ans,2))