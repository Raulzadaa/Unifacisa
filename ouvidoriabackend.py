from operacoesbd import *

def listarReclamacoes(conexao):
    consulta = 'SELECT * FROM reclamacoes'
    reclamacoes = listarBancoDados(conexao, consulta)

    if len(reclamacoes) > 0:
        print("Lista de Reclamações:")
        for item in reclamacoes:
            print(f"- Código: {item[0]} | Descrição: {item[1]}")
    else:
        print("Não existem reclamações!")


def adicionarReclamacoes(conexao):
    novaReclamacao = input("Digite sua reclamação: ")

    consulta = 'INSERT INTO reclamacoes (descricao) VALUES (%s)'
    dados = [novaReclamacao]

    codigoNovaReclamacao = insertNoBancoDados(conexao, consulta, dados)

    if codigoNovaReclamacao:
        print("Reclamação cadastrada com sucesso! Código:", codigoNovaReclamacao)
    else:
        print("Erro ao cadastrar reclamação.")


def pesquisarReclamacoes(conexao):
    codigoreclamacoes = int(input("Digite o código da reclamação: "))

    consulta = 'SELECT * FROM reclamacoes WHERE codigo = %s;'
    dados = [codigoreclamacoes]

    reclamacoes = listarBancoDados(conexao, consulta, dados)

    if len(reclamacoes) == 0:
        print("Não existe reclamação para o código informado.")
    else:
        print("Reclamação encontrada:", reclamacoes[0][1])


def removerReclamacoes(conexao):
    codigoReclamacaoRemover = int(input("Digite o código da reclamação a ser removido: "))

    consulta = 'DELETE FROM reclamacoes WHERE codigo = %s;'
    dados = [codigoReclamacaoRemover]

    quantidadeRemovidos = excluirBancoDados(conexao, consulta, dados)

    if quantidadeRemovidos == 0:
        print("Não existe reclamação para o código informado.")
    else:
        print("Reclamação removida com sucesso.")


def quantidadeReclamacoes(conexao):
    consulta = 'SELECT COUNT(*) FROM reclamacoes;'
    resultado = listarBancoDados(conexao, consulta)

    print("Temos atualmente", resultado[0][0], "reclamação(ões)")


def atualizarReclamacoes(conexao):
    novaReclamacao = input("Digite a nova reclamação: ")
    codigoReclamacao = int(input("Digite o código da reclamação a ser alterado: "))

    consulta = 'UPDATE reclamacoes SET descricao = %s WHERE codigo = %s;'
    dados = [novaReclamacao, codigoReclamacao]

    linhasAtualizadas = atualizarBancoDados(conexao, consulta, dados)

    if linhasAtualizadas == 0:
        print("Não existe uma reclamação para o código informado.")
    else:
        print("Reclamação atualizada com sucesso.")