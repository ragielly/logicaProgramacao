import os
from collections import deque
os.system('cls')

def criarPilha():
    return deque()

def insereNaPilha(pilha,elemento):
   pilha.append(elemento)

def removeDaFila(pilha):
    return pilha.pop()



pilha = criarPilha()


print(pilha)

insereNaPilha(pilha,8)
insereNaPilha(pilha,9)
insereNaPilha(pilha,10)
insereNaPilha(pilha,11)
insereNaPilha(pilha,12)
insereNaPilha(pilha,13)
print(f'Removendo: {removeDaFila(pilha)}')
print(f'Removendo: {removeDaFila(pilha)}')
print(pilha)
