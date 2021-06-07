import jogo_adivinhacao

def executar():
    def linha():
        print("-="*40)

    linha()
    print("Escolha seu Jogo")
    linha()

    opcao = int(input("Opção 01: Forca\nOpcao 02: Adivinhação\nDigite: "))

    while opcao != 1 and opcao != 2:
        opcao = int(input("Opção 01: Forca\nOpcao 02: Adivinhação\nDigite: "))
        linha()

    linha()

    if(opcao == 1):
        print("Jogando Forca")
    else:
        print("jogando Adivinhação")
        jogo_adivinhacao.jogar()


'''
Mesmo um módulo solitário, pode executar alguma funcionalidade
quando executado isoladamente, basta adicionar um if no final
do código para verigicar a variável __name__

'''
if __name__ == "__main__":
    executar()


