nome = print(str(input("Olá, qual seu nome?")))
n1 = float(input("Digite sua primeira nota"))
n2 = float(input("Digite sua segunda nota"))
m = (n1+n2)/2
if m >= 6.0:
    print("sua nota foi boa, parabéns")
else:
    print("Sua nota foi pessima, estude, mais{}".format(nome))

