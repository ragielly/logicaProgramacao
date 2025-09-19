from heapq import *

fila_prioridade = []

heappush(fila_prioridade,(3,'Atender cliente Vip'))
heappush(fila_prioridade,(2,'Situação Critica'))
heappush(fila_prioridade,(1,'Responder e-mails'))
heappush(fila_prioridade,(1,'Apagar incendio'))

while fila_prioridade:
    prioridade,tarefa = heappop(fila_prioridade)
    print(f'Executando:{tarefa} - Prioridade: {prioridade}')