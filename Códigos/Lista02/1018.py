def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    qtd_notas = []
    for nota in notas:
        quantidade = valor // nota
        qtd_notas.append(quantidade)
        valor %= nota
    return qtd_notas

valor = int(input())

print(valor)

notas = calcular_notas(valor)
for i, nota in enumerate([100, 50, 20, 10, 5, 2, 1]):
    print(f"{notas[i]} nota(s) de R$ {nota},00")
