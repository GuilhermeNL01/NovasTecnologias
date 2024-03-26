matriz = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
]

elementos_unicos = set()

for linha in matriz:
    for elemento in linha:
        elementos_unicos.add(elemento)

print("Elementos únicos na matriz:")
print(elementos_unicos)