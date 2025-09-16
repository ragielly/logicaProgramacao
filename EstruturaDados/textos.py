frase = ' O curso de Lógica de Programação é Legal'
# print(f'Primeira letra: {frase[0]}')
# print(f'Ultima letra: {frase[-1]}')
# print(f'Tamanho da frase: {len(frase)} caracteres')
# print()
# print(f'Maiúsculas:{frase.upper()}')
# print(f'Minusculas:{frase.lower()}')
# print()
# print(f'Fatiando: {frase.split()}')
# print(f'Fatiando onde tem A: {frase.split('a')}')
# print()
# print(f'Limpando: {frase.strip()}')
# print(f'Tamanho string limpa: {len(frase.strip())}')

def analizadorDeTexto(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    num_caracteres_sem_espacos = num_caracteres - texto.count(' ')
    return num_palavras, num_caracteres, num_caracteres_sem_espacos

num_p,num_c,num_cse = analizadorDeTexto(frase)

print(f'Numedo de palavras: {num_p}')
print(f'Numedo de  caracteres: {num_c}')
print(f'Numedo de  caracteres sem espaço: {num_cse}')