# 👉 Enunciado:
# Simule uma fila de atendimento bancário. As pessoas entram na fila,
# e o atendente chama na ordem.
# 👉 Enunciado:
# Simule uma fila de impressão. Cada documento entra na fila,
# e a impressora imprime em ordem.

from collections import deque

fila = deque()

def inserirCliente(fila,pessoa):
    fila.append(pessoa)

def atenderCliente(fila):
    fila.popleft()


print(fila)

inserirCliente(fila,'Maria')
inserirCliente(fila,'João')
inserirCliente(fila,'Jose')
inserirCliente(fila,'Antonia')

print(fila)

atenderCliente(fila)
atenderCliente(fila)
atenderCliente(fila)
print(fila)