lista_de_compras = ['maçã', 'banana', 'laranja']

aposta_mega_sena = [6, 14, 19, 20, 39, 53]

lista_nova = aposta_mega_sena[len(aposta_mega_sena)//2:] + lista_de_compras[:len(lista_de_compras)//2]
lista_nova = lista_nova * 2
print(lista_nova)
