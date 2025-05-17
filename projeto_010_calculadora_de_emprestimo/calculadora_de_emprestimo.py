def calcular_emprestimo(valor, taxa_juros_anual, anos):
    taxa_mensal = taxa_juros_anual / 100 / 12
    numero_de_parcelas = anos * 12

    if taxa_mensal == 0:
        parcela = valor / numero_de_parcelas
    else:
        parcela = valor * (taxa_mensal * (1 + taxa_mensal) ** numero_de_parcelas) / \
                  ((1 + taxa_mensal) ** numero_de_parcelas - 1)

    total_pago = parcela * numero_de_parcelas
    juros_total = total_pago - valor

    return parcela, total_pago, juros_total


# Entrada do usuário
print("=== Calculadora de Empréstimos ===")
valor = float(input("Valor do empréstimo (R$): "))
taxa = float(input("Taxa de juros anual (%): "))
anos = int(input("Prazo do empréstimo (em anos): "))

parcela, total, juros = calcular_emprestimo(valor, taxa, anos)

print(f"\nValor da parcela mensal: R$ {parcela:.2f}")
print(f"Total pago ao final do empréstimo: R$ {total:.2f}")
print(f"Total de juros pagos: R$ {juros:.2f}")
