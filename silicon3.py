estimates = [1,1,9,3,7,6,5,10]
k = int(input())

cache = [None] * len(estimates)
estimates.sort(reverse=True)
cache[0] = max(estimates)
for i in range(1,len(estimates)):
    cache[i] = max(0,cache[i-1]) + estimates[i]

print(cache)