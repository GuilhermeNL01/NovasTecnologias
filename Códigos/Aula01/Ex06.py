import random

numero_secreto = random.randint(1, 100)

while True:
  palpite = int(input("Digite um palpite entre um e 100: "))

  if palpite == numero_secreto:
    print("Você adivinhou o número!")
    break

  elif palpite > numero_secreto:
    print("Seu palpite foi maior que o número secreto. Tente novamente.")
  else:
    print("Seu palpite foi menor que o número secreto. Tente novamente.")