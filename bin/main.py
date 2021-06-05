import random


def linha():
    print("-="*40)

def funcao_tentativas(numero_escolhido,numero_secreto,c):
    global tentativa
    global pontos
    acertou = numero_escolhido == numero_secreto
    maior = numero_escolhido > numero_secreto
    menor = numero_escolhido < numero_secreto
    if acertou:
        print(f"Você acertou, o número é {numero_secreto}\nPONTUACAO: {pontos}")
        tentativa = 0
        linha()
    else:
        if maior:
            tentativa += 1
            print("Você errou, seu numero foi maior que o numero secreto")
            print(f"tentativa {tentativa}/{c}")
            numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            while numero_escolhido < 0 or numero_escolhido > 100:
                numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            linha()
            perda_pontos = abs(numero_escolhido - numero_secreto)
            pontos -= perda_pontos
            return numero_escolhido

        elif menor:
            tentativa += 1
            print("Você errou, seu numero foi menor que o numero secreto")
            print(f"tentativa {tentativa}/{c}")
            numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            while numero_escolhido < 0 or numero_escolhido > 100:
                numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
            linha()
            perda_pontos = abs(numero_escolhido - numero_secreto)
            pontos -= perda_pontos
            return numero_escolhido


tentativa = 0
pontos = 1000

linha()
print("Bem vindo ao jogo de adivinhação")
linha()


dificuldade = int(input("Nivel da dificuldade... \n(1)-Fácil\n(2)-Médio\n(3)-Difícil\nDigite: "))

linha()


while dificuldade != 1 and dificuldade != 2 and  dificuldade != 3:
    dificuldade = int(input("Nivel da dificuldade... \n(1)-Fácil\n(2)-Médio\n(3)-Difícil\nDigite: "))
    linha()


numero_secreto = random.randrange(1, 101)

numero_escolhido = int(input("Digite seu número entre 1 e 100: "))
while numero_escolhido < 0 or numero_escolhido > 100:
    numero_escolhido = int(input("Digite seu número entre 1 e 100: "))


linha()

if dificuldade == 1:
    for c in range(20):
        numero_escolhido = funcao_tentativas(numero_escolhido,numero_secreto,30)
        if numero_escolhido == numero_secreto:
            break

elif dificuldade == 2:
    for c in range(10):
        numero_escolhido = funcao_tentativas(numero_escolhido,numero_secreto,10)
        if numero_escolhido == numero_secreto:
            break

else:
    for c in range(5):
        numero_escolhido = funcao_tentativas(numero_escolhido,numero_secreto,5)
        if numero_escolhido == numero_secreto:
            break


    
    
    
if tentativa != 0:
    print(f"O número segreto era {numero_secreto}\nPONTUACAO: {pontos}")

print("Fim do Jogo")



