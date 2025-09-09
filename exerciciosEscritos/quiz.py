import os

os.system('cls')

perguntas = [
    ['Qual é a cor do céu em um dia claro?','azul'],
    ['Qual é o nome do animal que mia?','gato'],
    ['Qual fruta é amarela e curva?','banana'],
    ['Qual é o oposto de frio?','quente']
             ]
acertos = 0

print("------QUIZ------")
for pergunta in perguntas:

    resposta= input(pergunta[0] + "?")

    if resposta.lower() == pergunta[1]:
        acertos += 1
        print('acertou!!')
    else:
        print("errou!!")
        acertos += 0  
os.system('cls')
print(f'total de acertos {acertos}/ total de perguntas:{len(perguntas)}')