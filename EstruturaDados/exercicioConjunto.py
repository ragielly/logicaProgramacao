# Enunciado:
# Dadas duas listas de alunos:

# turma1 = ["Ana", "Bruno", "Carlos", "Daniela"]
# turma2 = ["Carlos", "Daniela", "Eduardo", "Fernanda"]


# Encontre os alunos que estão nas duas turmas.

# Encontre os alunos que estão apenas na turma1.

# Encontre todos os alunos sem repetição.

turma1 = ["Ana", "Bruno", "Carlos", "Daniela"]
turma2 = ["Carlos", "Daniela", "Eduardo", "Fernanda"]

setT1 = set(turma1)
setT2 = set(turma2)

# Encontre os alunos que estão nas duas turmas.
ambas = setT1 & setT2
print(f' alunos em ambas as turmas: {ambas}')

# Encontre os alunos que estão apenas na turma1.

sTurma1= setT1 - setT2
print(f'alunos presentes somente na turma 1: {sTurma1}')

# Encontre todos os alunos sem repetição.

uniao= setT1 | setT2
print(f'Turmas juntas: {uniao}')