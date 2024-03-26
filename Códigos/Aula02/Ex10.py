
dias_semana = {
    "segunda-feira": "Monday",
    "terça-feira": "Tuesday",
    "quarta-feira": "Wednesday",
    "quinta-feira": "Thursday",
    "sexta-feira": "Friday",
    "sábado": "Saturday",
    "domingo": "Sunday"
}

while True:
    dia = input("Digite o dia da semana em português (ou 'fim' para encerrar): ")
    if dia == 'fim':
        print("Programa encerrado.")
        break
    elif dia in dias_semana:
        print(f"A tradução de '{dia}' é '{dias_semana[dia]}'.")
    else:
        print("Dia não encontrado no dicionário.")
