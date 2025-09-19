lista = {'valor':5,'proximo':None}

def exibeLista():
   
    if not lista:
        print('Lista vazia')
        return
    elemento = lista
    
    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']

    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = { 'valor' : elemento, 'proximo': None}
        return    
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor':elemento, 'proximo':None}

exibeLista()
adicionaNoFim(1)
adicionaNoFim(8)
exibeLista()