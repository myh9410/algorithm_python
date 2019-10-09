array = [1, 5, 2, 6, 3, 7, 4]
answer=[]
commands = [[2,5,3,],[4,4,1],[1,7,3]]

for elements in commands:
    i = elements[0]
    j = elements[1]
    k = elements[2]
    subarr = array[i-1:j]
    subarr.sort()
    answer.append(subarr[k-1])

print(answer)