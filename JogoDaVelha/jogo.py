# Exemplo resumido da criação de um tabuleiro:
# tabuleiro = [ ['' for _ in range(3)] for _ in range(3)]

tabuleiro = [
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' '],
    [' ' , ' ' , ' ']
]

jogador= 'X'

def exibeTabuleiro():
   for linha in tabuleiro:
        #print(f'{linha[0]}|{linha[1]}|{linha[2]}')
        print('|'.join(linha))
        print('-'*5)

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

def temGanhador():

# """ verifica as linhas """
    for linha in range(3):
        if(
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU!!!')
            return True
# """ verifica as coluna """
    for coluna in range(3):
        if(
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[coluna][0]} GANHOU!!')
            return True
# verificar diagonal \

    if(
        tabuleiro[1][1] != ' ' and 
        tabuleiro[0][0] == tabuleiro[1][1] and
        tabuleiro[0][0] == tabuleiro[2][2]
    ):
        print(f'{tabuleiro[0][0]} GANHOU!!!')
        return True
# verificar diagonal /

    if(
        tabuleiro[1][1] != ' ' and
        tabuleiro[0][2] == tabuleiro[1][1] and
        tabuleiro[0][2] == tabuleiro[2][0]
    ):
        print(f'{tabuleiro[0][2]} GANHOU!!!')
        return True


def temEmpate():
    for linhas in range(3):
        for colunas in range(3):
            if tabuleiro[linhas][colunas] == ' ':
               return False
    print('Acabou em empate!!')
    return True

while True:
    print(f'Jogador da vez:{jogador}')
    try:
        linha = int(input('Digite a linha:'))
        coluna = int(input('Digite a coluna:'))
        jogador = jogada(linha,coluna)
    except IndexError:
        print('Digite valores numéricos entre 0 e 2!')
    except ValueError:
        print('Os valores devem ser números inteiros!')        
    exibeTabuleiro()
    if temGanhador() or temEmpate():
        break
