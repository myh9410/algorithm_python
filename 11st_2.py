import math
balloons = [[2, 2], [4, 4], [1, 4], [-1, -4]]
dict = {}
for i in balloons:
    count = dict.get(math.atan2(i[1],i[0]),0)
    dict[math.atan2(i[1],i[0])] = count+1

print(len(dict))
