# Gerador de Tabuadas - Salvando em arquivo

def gerar_tabuadas():
    inicio = int(input("Gerar tabuadas a partir de qual número? "))
    fim = int(input("Até qual número? "))
    nome_arquivo = "tabuadas.txt"

    with open(nome_arquivo, "w") as arquivo:
        for numero in range(inicio, fim + 1):
            arquivo.write(f"Tabuada do {numero}:\n")
            for i in range(1, 11):
                resultado = numero * i
                arquivo.write(f"{numero} x {i} = {resultado}\n")
            arquivo.write("\n")  # Linha em branco entre as tabuadas

    print(f"\nTabuadas de {inicio} até {fim} foram salvas no arquivo '{nome_arquivo}'.")

gerar_tabuadas()
