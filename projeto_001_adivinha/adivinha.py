from random import randint

sorteado = randint(1, 10)

vidas = 3

while True:
    palpite = int(input("Digite um número: "))

    if palpite == sorteado:
        print("Você acertou!")
        break

    if palpite < sorteado:
        print("O número sorteado é maior que o chute.")
    elif palpite > sorteado:
        print("O número sorteado é menor que o chute.")

    vidas -= 1

    if vidas == 0:
        print("Você perdeu!")
        break