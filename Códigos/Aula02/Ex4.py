lista_vazia = []
for i in range(len(aposta_mega_sena)):
    if aposta_mega_sena[i] not in lista_vazia:
        lista_vazia.append(aposta_mega_sena[i])
lista_vazia.sort(reverse=True)
print(lista_vazia)