num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while num1 == num2:
    print("Os números são iguais. Por favor, insira o segundo número novamente.")
    num2 = float(input("Digite o segundo número: "))

if num1 < num2:
    print("O primeiro número é menor:", num1)
else:
    print("O segundo número é menor:", num2)
