matriz = [[0 for x in range(5)] for x in range(5)]
for i in range(5):
    for j in range(5):
        matriz[i][j] = i + j
print(matriz)