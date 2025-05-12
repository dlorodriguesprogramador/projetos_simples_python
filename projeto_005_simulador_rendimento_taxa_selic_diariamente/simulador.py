import datetime

def calcular_taxa_diaria_selic(selic_anual):
    return (1 + selic_anual) ** (1 / 252) - 1

def obter_dias_uteis(data_inicio, dias_uteis):
    dias = []
    atual = data_inicio
    while len(dias) < dias_uteis:
        if atual.weekday() < 5:  # 0 a 4 são dias úteis (seg a sex)
            dias.append(atual)
        atual += datetime.timedelta(days=1)
    return dias

def simular_rendimento(valor_inicial, selic_anual, dias_uteis):
    taxa_diaria = calcular_taxa_diaria_selic(selic_anual)
    saldo = valor_inicial
    historico = []
    datas = obter_dias_uteis(datetime.date.today(), dias_uteis)

    for data in datas:
        rendimento = saldo * taxa_diaria
        saldo += rendimento
        historico.append((data.strftime("%d/%m/%Y"), saldo, rendimento))

    return historico

# ----- Entrada do usuário -----
valor_inicial = float(input("Valor inicial investido (R$): "))
selic_anual = float(input("Taxa Selic atual (% ao ano): ")) / 100
dias_uteis = int(input("Quantos dias úteis deseja simular? "))

# ----- Executa a simulação -----
resultado = simular_rendimento(valor_inicial, selic_anual, dias_uteis)

# ----- Exibe os resultados -----
print("\nSimulação de rendimento diário (100% da Selic):\n")
for data, saldo, rendimento in resultado:
    print(f"{data} | Saldo: R${saldo:.2f} | Rendimento do dia: R${rendimento:.2f}")

lucro_total = resultado[-1][1] - valor_inicial
print(f"\nLucro total após {dias_uteis} dias úteis: R${lucro_total:.2f}")