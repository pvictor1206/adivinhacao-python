def linha():
    print('=-'*40)

def jogar():
    linha()
    print('Jogo da forca')
    linha()

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
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
        print(letras_acertadas)

if __name__ == '__main__':
    jogar()

