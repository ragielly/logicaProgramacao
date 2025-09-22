texto = 'Naruto é uma das obras mais famosas do mundo dos animes e mangás, criada por Masashi Kishimoto. A história acompanha Naruto Uzumaki, um jovem ninja que carrega dentro de si a raposa de nove caudas, uma criatura poderosa que atacou sua vila no passado. Rejeitado por muitos e tratado como um pária, ele cresce com o sonho de se tornar Hokage, o líder de sua aldeia, para ganhar o reconhecimento e respeito de todos. Sua jornada é marcada por treinamentos intensos, batalhas emocionantes e laços de amizade que moldam sua personalidade e seu destino.'


palavras = texto.split()
tabela = {}

for palavra in palavras:
    indice = palavra[0].lower()
    if indice not in tabela:
        tabela[indice] = []
    tabela[indice].append(palavra)

for chave,valor in tabela.items():
    print(f'{chave}: {len(valor)}')

