# 👉 Enunciado:
# Use uma pilha para verificar se uma palavra é palíndromo
# (ou seja, se pode ser lida da mesma forma de frente para trás).
# 👉 Enunciado:
#Converta um número decimal para binário usando pilha.


from collections import deque

def verifica_polindromo(palavra):

    pilha=deque()

    for letra in palavra:
        pilha.append(letra)
    
    invertido=""

    while pilha:
        invertido+= pilha.pop()
    return palavra == invertido

palavra = input('Digite uma palavra: ')
resultado = verifica_polindromo(palavra)
print(f'A palavra invertida  {palavra} é {resultado}')
