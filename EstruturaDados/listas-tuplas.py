import os 

os.system('cls')
lista = [1,2,3,4]
tupla = (1,2,3,4)


tarefas=[]

def adicionarTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibeTarefas():
    if not tarefas :
        print('++++Lista de tarefa Vazia++++')
        return
    for tarefa in tarefas:
        print(f'Tarefa : {tarefa[0]}  -  Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefas = [(t[0],'concluida') if t[0]== tarefa else t for t in tarefas]
    # novaLista = []
    # for t in tarefas:
    #     if t[0] ==tarefa:
    #         novaLista.append((tarefa,'concluida'))
    #     else:
    #         novaLista.append(t)
    # tarefas = novaLista
def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0]!= tarefa]

def buscarTarefa(tarefa):
    for t in tarefas:
        if t[0] == tarefa:
            print(f'Tarefa encontrada: {t[0]} -  Status: {t[1]}')

while True:
    os.system('cls')
    print('++++++Gerenciador Lista de tarefas+++++')
    print()
    print('1 - Listar tarefas')
    print('2 - Adicionar tarefa')
    print('3 - Remover tarefa')
    print('4 - Marcar concluida')
    print('5 - Buscar tarefa')
    print('0 - Sair')
    
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            exibeTarefas()
        case 2:
            tarefa = input('Digite uma tarefa: ')
            adicionarTarefa(tarefa)
        case 3:
            tarefa = input('Digite uma tarefa: ')
            removerTarefa(tarefa)
        case 4:
            tarefa = input('Digite uma tarefa: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('Digite uma tarefa: ')
            buscarTarefa(tarefa)
        case 0:
            print('Sair')
            break
        case _:
            print('Não entendi seu comando')
            break
    print()
    input('Precione ENTER para continuar...')
    