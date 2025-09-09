import os


os.system('cls')

print("O Oraculo que saber....")
print("1-Variáveis")
print("2-Operadores")
print("3-Estrutura de controle")
print("4-Loops")
print("5-Estrutura de Dados/Lista")
print("6-Tuplas")
print("7-Dicionário")
print("8-Conjuntos")
print("9-Funções")

opcao = int(input("O que você deseja saber de python?(funcoes,loops,variaveis e listas) "))
os.system('cls')
match opcao:
    case 1:
        print("As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas.")
    case 2:
        print("Os operadores são símbolos especiais que nos permitem realizar operações em variáveis e valores")
    case 3:
        print("As estruturas de controle nos permitem controlar o fluxo de execução de nossos programas")
    case 4:
        print("Os loops nos permitem repetir um bloco de código várias vezes.")
    case 5:
        print("As estruturas de dados nos permitem organizar e armazenar dados de maneira eficiente em nossos programas. ")
    case 6:
        print("Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos.")
    case 7:
        print("Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor")
    case 8:
        print("Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor")
    case 9:
        print("As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário")
    case _:
        print(" Oráculo responde que ainda está aprendendo.")