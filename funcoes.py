def olaMundo():
    print('Ola mundo!')

def olaPessoa(nome):
    print(f'Ola, {nome}!')

def dobro(numero):
    return numero * 2

#print(dobro(5)+2)

def multiplicaDoisNumeros(a,b=2):
    """multiplica dois numeros"""
    return a*b

#print(multiplicaDoisNumeros(3,5))

x = 5 # Variável global
def soma():
    x = 10 # Variável local
    print(x)
    return x + 1 
soma()
print(x)