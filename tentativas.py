from random import randint
from time import sleep
computador = randint(0,5)
print("=-"* 25)
print("Estou pensando em um número, tente adivinhar...")
print("=-"* 25)
jogador= int(input("Qual número estou pensando?"))
print("Analisando...")
sleep(3)
if jogador== computador:
    print("Parabéns voc~e acertou")
else:
    print("Você errou!!!!")

