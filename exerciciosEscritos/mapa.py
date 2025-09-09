import os
os.system('cls')

mapa= [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]


linhaT=1
colunaT=2

def exibemapa():
    for linha in mapa:
        print('|'.join(linha))
        print('-----')


print("++++++++++Acerte onde está o tesouro no mapa++++++++++++++++++")
print("5 tentativas")


for index in range(5):
    linha = input("Digite a linha:")
    coluna = input("Digite a coluna:")

    exibemapa()