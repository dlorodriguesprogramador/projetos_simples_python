import random

def gerar_jogo():
    return sorted(random.sample(range(1, 26), 15))

def gerar_varios_jogos(quantidade):
    jogos = []
    for _ in range(quantidade):
        jogo = gerar_jogo()
        jogos.append(jogo)
    return jogos

# Quantidade de jogos a gerar
qtd = int(input("Quantos jogos deseja gerar? "))

jogos_gerados = gerar_varios_jogos(qtd)

# Mostrar os jogos
for i, jogo in enumerate(jogos_gerados, 1):
    print(f"Jogo {i}: {jogo}")