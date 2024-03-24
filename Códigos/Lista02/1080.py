maior_numero = 0
posicao_maior_numero = 0

for i in range(1, 101):
    numero = int(input())
    
    if numero > maior_numero:
        maior_numero = numero
        posicao_maior_numero = i

print(maior_numero)
print(posicao_maior_numero)
