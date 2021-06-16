def linha():
    print('=-'*40)

def jogar():
    linha()
    print('Jogo da forca')
    linha()

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = str(input("Qual letra?: "))

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {letra} na posicao {index+1}")
            index += 1

if __name__ == '__main__':
    jogar()

