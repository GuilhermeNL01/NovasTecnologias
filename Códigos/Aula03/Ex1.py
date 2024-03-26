def comparar_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    valores_comuns = list(conjunto1.intersection(conjunto2))
    
    valores_apenas_lista1 = list(conjunto1.difference(conjunto2))
    
    valores_apenas_lista2 = list(conjunto2.difference(conjunto1))
    
    return valores_comuns, valores_apenas_lista1, valores_apenas_lista2

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comuns, apenas_lista1, apenas_lista2 = comparar_listas(lista1, lista2)

print("Valores que aparecem nas duas listas:", comuns)
print("Valores que aparecem apenas na primeira lista:", apenas_lista1)
print("Valores que aparecem apenas na segunda lista:", apenas_lista2)
