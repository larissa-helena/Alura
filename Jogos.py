import aula
import Forca

print("**********************************")
print("*********Escolha seu jogo!********")
print("**********************************")

print("1 - Forca  2 - Advinhação")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Jogando forca")
    Forca.jogar()

elif jogo == 2:
    print("Jogando advinhação")
    aula.jogar()