def contamatrizlista(matriz, lista):
    contagens = []
    for numero in lista:
        contagem = sum(linha.count(numero) for linha in matriz)
        contagens.append(contagem)
    return contagens

matriz = [[1,2,3,4,5],[2,3,4,5,8],[3,9,5,6,7],[4,5,8,7,8]]
lista = [1,2,3,8]
print(contamatrizlista(matriz, lista))
