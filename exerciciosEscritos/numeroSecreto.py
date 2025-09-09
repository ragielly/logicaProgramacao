import os

os.system('cls')

secreto= 17
tentativas=0

print("--------Acerte o numero secreto---------")
while True:
    numero= int(input("Digite o numero secreto:"))

    if numero == secreto:
        print("Acertou!!")
        break
    else:
        tentativas +=1
os.system('cls')
print(f"Total tentativas :{tentativas} o numero secreto é :{secreto}")    