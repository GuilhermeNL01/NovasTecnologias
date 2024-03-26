entrada = [0, 0, 0, 1, 0, 0, 5, 0]

dicionario = {indice: valor for indice, valor in enumerate(entrada) if valor != 0}

print("Dicionário resultante:", dicionario)

lista_reconstruida = [dicionario.get(i, 0) for i in range(len(entrada))]

print("Lista reconstruída:", lista_reconstruida)
