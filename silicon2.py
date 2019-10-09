office = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]]
k = 2
matrix = [[0]*(k) for _ in range(k)]
print(matrix)

for i in range(len(office)):
    for j in range(len(office[i])):
        matrix[i][j] = office[i][j]
        print(i,j)
        print(matrix)

