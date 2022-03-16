import random

def jogar():

    print("**********************************")
    print("bem vindo ao jogo de adivinhação")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print ("Níveis")
    print ("1 - Fácil  2 - Médio  3 - Difícil")

    nivel = int(input("Defina um nível: "))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range (1, tentativas):
        print("tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("digite o seu número entre 1 e 100: ")
        print("voce digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print ("você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("seu chute foi maior do que o numero secreto")
            elif menor:
                print("seu numero foi menor que o numero secreto")
            perdidos = abs(numero_secreto - chute)
            pontos = pontos - perdidos

    print("fim do jogo")

if(__name__=="__main__"):
    jogar()