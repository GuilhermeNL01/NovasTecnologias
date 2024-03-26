meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
posição = "primeiro","segundo","terceiro","quarto","quinto","sexto","sétimo","oitavo","nono","décimo","décimo primeiro","décimo segundo"

while True:
    escolha = input("Escolha um mês: ") 
    if escolha in meses:
        print(escolha.capitalize(), "é o", posição[meses.index(escolha)], "mês do ano.")
        break  
    else:
        print("escolha um mês válido.")