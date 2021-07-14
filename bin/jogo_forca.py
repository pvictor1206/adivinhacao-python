import random

def linha():
    print('=-'*40)

def jogar():
    linha()
    print('Jogo da forca')
    linha()

    arquivo = open("palavra.txt","r")
    palavras = list()

    for c in arquivo:
        c = c.strip()
        palavras.append(c)


    arquivo.close()

    sorteio = random.randrange(0,len(palavras))
    

    palavra_secreta = palavras[sorteio]
    letras_acertadas = list()

    for lentra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = str(input("Qual letra?: ")).lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    

if __name__ == '__main__':
    jogar()

