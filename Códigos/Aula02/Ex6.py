valor_buscado = int(input("Digite um valor: "))
encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == valor_buscado:
            encontrado = True
            print(f"O valor {valor_buscado} foi encontrado na linha {i} e coluna {j}.")
            break
    if encontrado:
        break
if not encontrado:
    print(f"O valor {valor_buscado} não foi encontrado na matriz.")