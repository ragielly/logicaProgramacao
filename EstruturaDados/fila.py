import os
from collections import deque
os.system('cls')

def criarFila():
    return deque()

def insereNaFila(fila,elemento):
    fila.append(elemento)

def removeDaFila(fila):
    return fila.popleft()



fila = criarFila()


print(fila)

insereNaFila(fila,8)
insereNaFila(fila,9)
insereNaFila(fila,10)
insereNaFila(fila,11)
insereNaFila(fila,12)
insereNaFila(fila,13)
print(f'Removendo: {removeDaFila(fila)}')
print(f'Removendo: {removeDaFila(fila)}')
print(fila)
