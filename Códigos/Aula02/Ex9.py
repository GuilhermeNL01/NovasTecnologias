dias_semana = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")

while True:
    primeiro_dia_semana = input("Em que dia da semana caiu o primeiro dia do mês? ")
    if primeiro_dia_semana in dias_semana:
        primeiro_dia_index = dias_semana.index(primeiro_dia_semana)
        break
    else:
        print("Por favor, insira um dia da semana válido.")

print("\nCalendário Simplificado:")

print("Dia da Semana")

for dia in range(1, 32):
    dia_da_semana = dias_semana[(dia + primeiro_dia_index - 1) % 7]
    print(f"{dia}\t| {dia_da_semana}")
