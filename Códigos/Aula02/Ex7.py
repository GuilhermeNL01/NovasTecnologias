def contar_sequencias(texto1, texto2):
    contagem = 0
    for i in range(len(texto1) - 2):  
        sequencia = texto1[i:i+3]     
        if sequencia in texto2:
            contagem += 1
    return contagem


texto1 = input("Digite o primeiro texto: ")
texto2 = input("Digite o segundo texto: ")


quantidade = contar_sequencias(texto1, texto2)


print("Quantidade de sequências de 3 caracteres do primeiro texto presentes no segundo texto:", quantidade)
