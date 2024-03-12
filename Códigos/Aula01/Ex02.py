# Escreva um trecho de código que leia um valor numérico do teclado e que imprima a área de um círculo com esse raio (área do círculo = 3.1415 * R^2). Garanta que o resultado seja um número real (float).

raio = float(input("Digite o raio do círculo: "))
area = 3.1415 * raio**2
print("A área do círculo é", area)
