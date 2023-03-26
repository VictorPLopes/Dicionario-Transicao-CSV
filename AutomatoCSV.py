# Por: Victor Probio Lopes - Engenharia de Computação
# Algoritmo original por: Prof. Dr. Osvaldo Severino Junior - IFSP - Campus Piracicaba


import csv  # Importa a biblioteca para trabalhar com arquivos CSV


# Cria o dicionário de transição a partir de um arquivo CSV
# Função criaTransicao, com o parâmetro arquivo (nome do arquivo CSV)
def criaTransicao(nomeArquivo, debug=False):
    with open(nomeArquivo) as arquivo:  # Abre o arquivo CSV
        leitor = csv.reader(arquivo, delimiter=';')  # Lê o arquivo CSV

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
        print(f'DEBUG:\n    {dicionarioTransicao}\n')

    return dicionarioTransicao  # Retorna o dicionário de transição


# Definição do autômato
# Função autômato, com os parâmetros: palavras, transicao (dicionário de transição), estado inicial padrão, estados finais e debug (para mostrar o estado atual e o próximo estado)
def automato(palavras, transicao, estadoInicial='q0', estadosFinais='qf', debug=False):
    reconhecidas = []  # Lista inicialmente vazia das palavras reconhecidas

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
                    print(f'    Proximo estado: {estadoAtual}')
            # Sai do for ao ler toda a palavra

            # Se o estado final for um dos estados finais (começa com qf)
            if estadoAtual.startswith(estadosFinais):
                # A palavra é reconhecida e adicionada à lista
                reconhecidas.append(palavra)
            else:  # Se não alcançar o estado final
                # Rejeita a palavra
                print(f'Palavra "{palavra}" rejeitada - não alcançou um estado final.')

        except:  # Se ocorrer uma exceção
            # Rejeita a palavra
            print(f'Palavra "{palavra}" rejeitada - transição de estados inválida presente.')
            continue  # Vai para a próxima palavra

    # Retorna a lista de palavras reconhecidas
    return f'Palavras aceitas: {reconhecidas}'


# Teste
while True:  # Loop infinito
    try:  # Tenta criar o dicionário à partir do arquivo
        # Chama a função criaTransicao com o nome do arquivo CSV e armazena o dicionário em transicao
        transicao = criaTransicao(input('Informe o nome do arquivo CSV: '))
        break  # Se conseguir carregar o arquivo, sai do loop

    except Exception as e:  # Se não encontrar o arquivo
        # Continua no loop
        print(f'Arquivo não encontrado ou com erros: {e}\nVerifique o nome digitado e os conteúdos do arquivo e tente novamente.')

while True:  # Loop infinito
    # Armazena o nome do arquivo de texto da cadeia, ou entra no modo de leitura manual
    arquivoTexto = input("Informe o nome do arquivo de texto com as palavras, ou pressione ENTER para inserir as palavras manualmente: ")

    if not arquivoTexto:  # Se a entrada for vazia, entra no modo de leitura manual
        while True:  # Loop infinito
            # entrada de dados
            palavras = input('Informe a(s) palavra(s) para testar (separadas por espaço) ou pressione ENTER para sair: ').split()
            if not palavras:  # Se a palavra for vazia
                quit()  # Sai do programa

            # Chama a função automato com a palavra e o dicionário
            print(automato(palavras, transicao))

    else:  # Se a entrada não for vazia, entra no modo de leitura de arquivo
        try:  # Tenta ler o arquivo
            # Caso haja um arquivo para ser lido, realiza a leitura
            with open(arquivoTexto) as arquivo:
                palavras = []  # Cria uma lista vazia para as palavras no arquivo

                for linha in arquivo.readlines():  # Para cada linha do arquivo
                    # Adiciona cada uma das palavras à lista
                    palavras.extend(linha.split())

                # Chama a função automato com a cadeia e o dicionário
                print(automato(palavras, transicao))
                break  # Sai do programa após a execução

        except Exception as e:  # Se não encontrar o arquivo
            # Continua no loop
            print(f'Arquivo não encontrado ou com erros: {e}\nVerifique o nome digitado e os conteúdos do arquivo e tente novamente.')