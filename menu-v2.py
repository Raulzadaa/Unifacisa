"""
1 - Isabel Luiza de Oliveira Sena
2 - Raul Ramses Neves Antao da Silva
3 - Guilherme Souto Rodrigues
"""


from operacoesbd import criarConexao, encerrarConexao
import ouvidoriabackend 

conexao = criarConexao('localhost', 'root', 'root1456','ouvidoria_isabel')

while True:
    print("\n1) Listar \n2) Adcionar \n3) Pesquisar pelo Código \n4) Remover \n5) Quantidade \n6) Atualizar \n7) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        ouvidoriabackend.listarReclamacoes(conexao)

    elif opcao == 2:
        ouvidoriabackend.adicionarReclamacoes(conexao)

    elif opcao == 3:
        ouvidoriabackend.pesquisarReclamacoes(conexao)

    elif opcao == 4:
        ouvidoriabackend.removerReclamacoes(conexao)

    elif opcao == 5:
        ouvidoriabackend.quantidadeReclamacoes(conexao)

    elif opcao == 6:
        ouvidoriabackend.atualizarReclamacoes(conexao)

    elif opcao == 7:
        break

encerrarConexao(conexao)
print("\n0brigada por usar o aplicativo!")