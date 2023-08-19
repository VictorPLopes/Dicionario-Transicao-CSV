versao = "1.1.0"  # Versão do programa

import csv  # Importa a biblioteca para trabalhar com arquivos CSV
import tkinter as tk  # Importa a biblioteca para trabalhar com a interface gráfica
from tkinter import filedialog  # Importa a função para abrir o explorador de arquivos
from tkinter import messagebox  # Importa a função para mostrar mensagens
import json  # Importa a biblioteca para trabalhar com arquivos JSON

root = tk.Tk()  # Cria a janela principal
root.withdraw()  # Esconde a janela principal


# Cria o dicionário de transição a partir de um arquivo CSV
# Função criaTransicao, com o parâmetro arquivo (nome do arquivo CSV)
def criaTransicao(nomeArquivo, debug=False):
    with open(nomeArquivo) as arquivo:  # Abre o arquivo CSV
        leitor = csv.reader(arquivo, delimiter=";")  # Lê o arquivo CSV

        # Cria uma lista de terminais a partir da primeira linha do arquivo CSV
        terminais = next(leitor)
        dicionarioTransicao = {}  # Cria um dicionário vazio para armazenar as transições

        for linha in leitor:  # Para cada linha subsequente do arquivo CSV
            estadoAtual = linha[0]  # O estado atual é o primeiro item da linha
            # Cria um dicionário vazio para a transição, com o estado atual como chave
            dicionarioTransicao[estadoAtual] = {}

            for i in range(1, len(linha)):  # Para cada novo estado (item) da linha
                if linha[i]:  # Se o item não for vazio
                    # Adiciona o novo estado no dicionário
                    dicionarioTransicao[estadoAtual][terminais[i]] = linha[i]

    if debug:  # Se o debug estiver ativado
        # Imprime o dicionário de transição
        print(f"DEBUG:\n    {dicionarioTransicao}\n")

    return dicionarioTransicao  # Retorna o dicionário de transição


# Definição do autômato
# Função autômato, com os parâmetros: palavras, transicao (dicionário de transição), estado inicial padrão, estados finais e debug (para mostrar o estado atual e o próximo estado)
def automato(
    palavras,
    transicao,
    tokens=None,
    estadoInicial="q0",
    estadosFinais="qf",
    palavrasReservadas="qf1",
    debug=False,
):
    palavrasAceitas = []  # Tabela de símbolos, inicialmente vazia

    for palavra in palavras:  # Para cada palavra na lista de palavras
        estadoAtual = estadoInicial  # Volta para o estado inicial

        try:  # Pode ocorrer uma exceção (erro) para palavras que não são reconhecidas
            for letra in palavra:  # Para cada letra da palavra
                if debug:  # Se o debug estiver ativado
                    # Estado atual e a letra lida
                    print(f'DEBUG:\n    Estado atual: "{estadoAtual}" | letra: {letra} | palavra: {palavra}')

                # Novo estado, partindo do estado atual e da letra lida
                estadoAtual = transicao[estadoAtual][letra]

                if debug:
                    # Próximo estado
                    print(f"    Proximo estado: {estadoAtual}")
            # Sai do for ao ler toda a palavra

            # Se não alcançar o estado final - rejeita a palavra
            if not estadoAtual.startswith(estadosFinais):
                print(f'Palavra "{palavra}" rejeitada - não alcançou um estado final.')
                continue  # Vai para a próxima palavra

            # Se alcançar o estado final mas não foi solicitada a análise léxica
            if not tokens:  # Caso não seja feita a análise léxica
                palavrasAceitas.append(palavra)  # Adiciona a palavra à lista de palavras aceitas
                continue  # Vai para a próxima palavra

            # Se alcançar o estado final e foi solicitada a análise léxica
            if estadoAtual != palavrasReservadas:  # Se não for o estado final das palavras reservadas
                palavrasAceitas.append([palavra, tokens[estadoAtual]])  # Adiciona a palavra e o token à tabela de símbolos
                continue  # Vai para a próxima palavra
            if palavra in tokens[palavrasReservadas]:  # Se a palavra estiver na lista de palavras reservadas
                palavrasAceitas.append([palavra, palavra])  # Adiciona a palavra e o token à tabela de símbolos
            else:  # Se a palavra não estiver na lista de palavras reservadas, é um nome de variável
                palavrasAceitas.append([palavra, "var"])  # Adiciona a palavra e o token à tabela de símbolos

        except:  # Se ocorrer uma exceção
            # Rejeita a palavra
            print(f'Palavra "{palavra}" rejeitada - transição de estados inválida presente.')
            continue  # Vai para a próxima palavra

    # Retorna a lista de palavras reconhecidas
    return palavrasAceitas


# Execução do programa
print(
    f"""AutomatoCSV v{versao} - Reconhecedor de palavras e analisador léxico
        Por: Victor Probio Lopes - Engenharia de Computação | https://github.com/VictorPLopes
        Com base em algoritmos por Prof. Dr. Osvaldo Severino Junior | IFSP - Campus Piracicaba\n
    """
)
input("Pressione ENTER para iniciar o programa.\n\n")  # Pausa o programa

debug = messagebox.askyesno("Debug", "Deseja ativar as informações de debug?")  # Pergunta se o usuário deseja ativar o debug

try:  # Tenta criar o dicionário à partir do arquivo
    # Chama a função criaTransicao com o nome do arquivo CSV e armazena o dicionário em transicao
    input("Pressione ENTER para selecionar o arquivo CSV com a tabela de transição.")  # Pausa o programa
    arquivoCSV = filedialog.askopenfilename()  # Abre a janela para selecionar o arquivo
    if not arquivoCSV:  # Se o arquivo não for selecionado
        input("Operação cancelada.\n Pressione ENTER para sair.")  # Pausa o programa
        quit()  # Sai do programa
    transicao = criaTransicao(arquivoCSV, debug=debug)
    print(f"Arquivo CSV {arquivoCSV} lido com sucesso.\n")
except Exception as e:  # Se houver algum erro
    input("Erro ao ler o arquivo: {e}\nVerifique os conteúdos do arquivo e tente novamente.\n Pressione ENTER para sair.")  # Pausa o programa
    quit()  # Sai do programa

# Armazena o nome do arquivo de texto da cadeia, ou entra no modo de leitura manual
if messagebox.askyesno("Modo de leitura", "Deseja ler as palavras de um arquivo de texto?"):  # Se o usuário escolher ler um arquivo
    try:  # Tenta ler o arquivo
        # Caso haja um arquivo para ser lido, realiza a leitura
        with open(filedialog.askopenfilename()) as arquivo:
            palavras = []  # Cria uma lista vazia para as palavras no arquivo
            for linha in arquivo.readlines():  # Para cada linha do arquivo
                # Adiciona cada uma das palavras à lista
                palavras.extend(linha.split())
    except Exception as e:  # Se houver algum erro
        input("Erro ao ler o arquivo: {e}\nVerifique os conteúdos do arquivo e tente novamente.\n Pressione ENTER para sair.")  # Pausa o programa
        quit()  # Sai do programa
else:
    # Pede para o usuário digitar as palavras
    palavras = input("Informe a(s) palavra(s) para testar (separadas por espaço) ou pressione ENTER para cancelar e sair:\n").split()
    if not palavras:  # Se a palavra for vazia
        quit()  # Sai do programa

if messagebox.askyesno("Analise Léxica", "Deseja realizar a análise léxica da cadeia selecionada?"):  # Se o usuário escolher realizar a análise léxica
    input("Pressione ENTER para selecionar o arquivo JSON com os tokens da linguagem (assumindo que qf1 é o estado das palavras reservadas).\n")  # Pausa o programa
    try: # Tenta ler o arquivo
        with open(filedialog.askopenfilename()) as tokens: # Abre o arquivo JSON
            tokens = json.load(tokens)  # Carrega o arquivo JSON e armazena o dicionário
            print(f"Arquivo JSON lido com sucesso.\n\n")
            print(f"Palavras aceitas e categorizadas ([cadeia, token]):\n{automato(palavras, transicao, tokens, debug = debug)}\n", sep="\n") # Chama a função automato e imprime o resultado
            input("Pressione ENTER para sair...") # Pausa o programa
    except Exception as e:  # Se houver algum erro
        input("Erro ao ler o arquivo: {e}\nVerifique os conteúdos do arquivo e tente novamente.\n Pressione ENTER para sair.")  # Pausa o programa
        quit()  # Sai do programa
else:
    print(f"Palavras aceitas:\n{automato(palavras, transicao, debug = debug)}\n", sep="\n") # Chama a função automato e imprime o resultado
    input("Pressione ENTER para sair...") # Pausa o programa