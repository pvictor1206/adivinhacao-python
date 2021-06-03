import random


def linha():
    print("-="*40)


linha()
print("Bem vindo ao jogo de adivinhação")
linha()

numero_secreto = random.randrange(1, 101)

numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
while numero_escolhido < 0 or numero_escolhido > 100:
    numero_escolhido = int(input("Digite seu número entre 1 e 100: "))


linha()

tentativa = 0



for c in range(3):
    acertou = numero_escolhido == numero_secreto
    maior = numero_escolhido > numero_secreto
    menor = numero_escolhido < numero_secreto
    if acertou:
        print(f"Você acertou, o número é {numero_secreto}")
        linha()
        break
    else:
        if maior:
            tentativa += 1
            print("Você errou, seu numero foi maior que o numero secreto")
            print(f"tentativa {c+1}/3")
            numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            while numero_escolhido < 0 or numero_escolhido > 100:
                numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            linha()
        elif menor:
            tentativa += 1
            print("Você errou, seu numero foi menor que o numero secreto")
            print(f"tentativa {c+1}/3")
            numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            while numero_escolhido < 0 or numero_escolhido > 100:
                numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            linha()
    
if tentativa == 3:
    print(f"O número segreto era {numero_secreto}")

print("Fim do Jogo")



