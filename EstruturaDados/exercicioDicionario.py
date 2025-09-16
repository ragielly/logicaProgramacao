import os

os.system('cls')
# Enunciado:


# Crie um dicionário que armazene o nome e a nota de 3 alunos.

# Exiba a nota de um aluno específico.

# Calcule a média das notas.

# Descubra qual aluno teve a maior nota.

# Crie um dicionário que armazene o nome e a nota de 3 alunos.
alunos = {
    'João' : 9.5,
     'Maria': 7.6,
     'Antônio': 8.3
     }

# Exiba a nota de um aluno específico.

print(f'A nota de Maria é {alunos['Maria']}')

# Calcule a média das notas.

media = sum(alunos.values())/len(alunos)

print(f'a media das notas é : {media}')

# Descubra qual aluno teve a maior nota.

maior_nota = max(alunos, key=alunos.get)

print(f'Maior nota é {alunos[maior_nota]} do aluno: {maior_nota}')