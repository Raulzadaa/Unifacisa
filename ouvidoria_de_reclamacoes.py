"""
Descrição do Projeto – Sistema de Ouvidoria de Reclamações

Este projeto consiste no desenvolvimento de um Sistema de Ouvidoria para registro e gerenciamento de reclamações, utilizando a linguagem de programação Python. O objetivo é criar um programa simples que permita cadastrar, listar, pesquisar, atualizar e remover reclamações registradas pelos usuários.

O sistema deve ser desenvolvido utilizando estruturas básicas de programação em Python, incluindo:

    Listas para armazenar as reclamações;

    Laços de repetição como for e while;

    A função range() para auxiliar em percursos e contagens;

    Estrutura de menu interativo para o usuário escolher as opções do sistema.

O programa deverá possuir funcionalidades como:

    1 - Listar reclamações registradas;

    2 - Registrar uma nova reclamação;

    3 - Pesquisar uma reclamação pelo código;

    4 - Atualizar uma reclamação existente;

    5 - Remover uma reclamação pelo código;

    6 - Mostrar a quantidade total de reclamações cadastradas;

    7 - Opção para sair do sistema.
"""

reclamacoes = []
opcao = 1

while opcao != "7":
    print("-=-=-=" * 10)
    print("""   1- Listar reclamacoes registradas
    2- Registrar uma nova recalmacao
    3- Pesquisara uma reclamacao pelo codigo
    4- Atualizar uma reclamacao existente
    5- Remover uma reclamacao pelo codigoe
    6- Mostrar a quantidade total de reclamacoes cadastradas
    7- Sair do sistema""")
    opcao = input("O Que voce deseja fazer? ")
    
    if opcao == "1":
        if len(reclamacoes) > 0:
            for index,reclamacao in enumerate(reclamacoes):
                print(f"{index + 1} - {reclamacao}")
        else:
            print("Nenhuma reclamacao foi registrada")

    elif opcao == "2":
        reclamacao_adicionar = input(f"Digite sua reclamacao: ")
        reclamacoes.append(reclamacao_adicionar)

    elif opcao == "3":
        pesquisa_codigo = int(input("Digite qual codigo da reclamacao que voce deseja pesquisar: "))
        if  0 < pesquisa_codigo <= len(reclamacoes):
            print(f"Esta eh a reclamacao {pesquisa_codigo} - {reclamacoes[pesquisa_codigo-1]}")
        else:
            print("Codigo de reclamacao Invalido!!")

    elif opcao == "4":
        pesquisa_codigo = int(input("Digite qual codigo da reclamacao que voce deseja alterar: "))
        if 0 < pesquisa_codigo <= len(reclamacoes):
            nova_mensagem = input(f"Digite o qual sera a nova mensagem da reclamacao {pesquisa_codigo}: ")
            reclamacoes[pesquisa_codigo - 1] = nova_mensagem
        else:
            print("Codigo de reclamacao Invalido!!")
    
    elif opcao == "5":
        pesquisa_codigo = int(input("Digite qual codigo da reclamacao que voce deseja remover: "))
        if 0 < pesquisa_codigo <= len(reclamacoes):
            reclamacoes.pop(pesquisa_codigo - 1)
        else:
            print("Codigo de reclamacao Invalido!!")

    elif opcao == "6"
        print(f"A quantidade total de reclamacoes eh {len(reclamacoes)}")

    elif opcao != "7":
        print("Opcao Invalida!")

print("Obrigado pelo uso do sistema, infelizmente suas reclamacoes nao serao salvas pois nao foi solicitado pelos Stakeholders")