def jogar():
    print("**********************************")
    print("bem vindo ao jogo de Forca")
    print("**********************************")

    palavra_secreta = "banana"
    letras_acertadas =["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Escolha uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
            else:
                print()

        print(letras_acertadas)

    print("fim do jogo")

if(__name__=="__main__"):
    jogar()