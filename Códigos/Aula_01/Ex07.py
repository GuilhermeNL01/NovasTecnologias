import random

# Definindo o número secreto
numero_secreto = random.randrange(1, 100)

# Definindo o número de tentativas
numero_tentativas = 10

while numero_tentativas > 0:
  # Pedindo um palpite ao usuário
  palpite = int(input(f"Digite um palpite entre 1 e 100 (Tentativas restantes: {numero_tentativas}): "))

  # Verificando se o palpite é igual ao número secreto
  if palpite == numero_secreto:
    print("Você adivinhou o número secreto!")
    break

  # Dando dicas ao usuário
  elif palpite > numero_secreto:
    print("Seu palpite foi maior que o número secreto. Tente novamente.")
  else:
    print("Seu palpite foi menor que o número secreto. Tente novamente.")

  # Diminuindo o número de tentativas
  numero_tentativas -= 1

# Mensagem caso o usuário não acerte o número secreto
if numero_tentativas == 0:
  print("Você não conseguiu adivinhar o número secreto. O número era:", numero_secreto)
