"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba: "Desculpe, você deixou os campos vazios"
"""
idade = input('Digite sua idade: ')
nome = input('Digite seu nome: ')

if idade and nome:
    nome_invertido = (nome[::-1])
    n_letras = (len(nome))
    primeira_letra_nome = (nome[0])
    ultima_letra_nome = (nome[-1])
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')

    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {n_letras} letras')
    print(f'A primeira letra do seu nome é {primeira_letra_nome} ')
    print(f'A última letra do seu nome é {ultima_letra_nome}')
else:
    print('Desculpe, você deixou um dos campos vazios')


























