# Autômato Automático
# Por: Victor Probio Lopes - Engenharia de Computação
# Algoritmo original por: Prof. Dr. Osvaldo Severino Junior - IFSP - Campus Piracicaba



import csv # Importa a biblioteca para trabalhar com arquivos CSV


# Cria o dicionário de transição a partir de um arquivo CSV
def criaTransicao(nomeArquivo, debug = False): # Função criaTransicao, com o parâmetro arquivo (nome do arquivo CSV)
    with open(nomeArquivo) as arquivo: # Abre o arquivo CSV
        leitor = csv.reader(arquivo, delimiter=';') # Lê o arquivo CSV
        
        terminais = next(leitor) # Cria uma lista de terminais a partir da primeira linha do arquivo CSV
        dicionarioTransicao = {} # Cria um dicionário vazio para armazenar as transições
        
        for linha in leitor: # Para cada linha subsequente do arquivo CSV
            estadoAtual = linha[0] # O estado atual é o primeiro item da linha
            dicionarioTransicao[estadoAtual] = {} # Cria um dicionário vazio para a transição, com o estado atual como chave
            
            for i in range(1, len(linha)): # Para cada novo estado (item) da linha
                if linha[i]: # Se o item não for vazio
                    dicionarioTransicao[estadoAtual][terminais[i]] = linha[i] # Adiciona o novo estado no dicionário
                    
    if debug: # Se o debug estiver ativado
        print(f'DEBUG:\n    {dicionarioTransicao}\n') # Imprime o dicionário de transição
                    
    return dicionarioTransicao # Retorna o dicionário de transição


# Definição do autômato
def automato(palavras, transicao, estadoInicial = 'q0', estadosFinais = 'qf', debug = False): # Função autômato, com os parâmetros: palavras, transicao (dicionário de transição), estado inicial padrão, estados finais e debug (para mostrar o estado atual e o próximo estado)    
    reconhecidas = [] # Lista inicialmente vazia das palavras reconhecidas
    
    for palavra in palavras: # Para cada palavra na lista de palavras
        estadoAtual = estadoInicial # Volta para o estado inicial
        
        try: # Pode ocorrer uma exceção (erro) para palavras que não são reconhecidas
            for letra in palavra: # Para cada letra da palavra
                if debug: # Se o debug estiver ativado
                    print(f'DEBUG:\n    Estado atual: "{estadoAtual}" | letra: {letra} | palavra: {palavra}') # Estado atual e a letra lida
                    
                estadoAtual = transicao[estadoAtual][letra] # Novo estado, partindo do estado atual e da letra lida
                
                if debug:
                    print(f'    Proximo estado: {estadoAtual}') # Próximo estado
            # Sai do for ao ler toda a palavra
            
            if estadoAtual.startswith(estadosFinais): # Se o estado final for um dos estados finais (começa com qf)
                reconhecidas.append(palavra) # A palavra é reconhecida e adicionada à lista
            else: # Se não alcançar o estado final
                print(f'Palavra "{palavra}" rejeitada - não alcançou um estado final.') # Rejeita a palavra
        
        except: # Se ocorrer uma exceção
            print(f'Palavra "{palavra}" rejeitada - transição de estados inválida presente.') # Rejeita a palavra
            continue # Vai para a próxima palavra
        
    return f'Palavras aceitas: {reconhecidas}' # Retorna a lista de palavras reconhecidas


# Teste
while True: # Loop infinito
    try: # Tenta criar o dicionário à partir do arquivo
        transicao = criaTransicao(input('Informe o nome do arquivo CSV: ')) # Chama a função criaTransicao com o nome do arquivo CSV e armazena o dicionário em transicao
        break # Se conseguir carregar o arquivo, sai do loop
    
    except: print('Arquivo não encontrado! Verifique o nome digitado e tente novamente') # Se não encontrar o arquivo, continua no loop

while True: # Loop infinito
    arquivoTexto = input("Informe o nome do arquivo de texto com as palavras, ou pressione ENTER para inserir as palavras manualmente: ") # Armazena o nome do arquivo de texto da cadeia, ou entra no modo de leitura manual

    if not arquivoTexto: # Se a entrada for vazia, entra no modo de leitura manual
        while True: # Loop infinito
            palavras = input('Informe a(s) palavra(s) para testar (separadas por espaço) ou pressione ENTER para sair: ').split() # entrada de dados
            if not palavras: # Se a palavra for vazia
                quit() # Sai do programa
                
            print(automato(palavras, transicao)) # Chama a função automato com a palavra e o dicionário
    
    else: # Se a entrada não for vazia, entra no modo de leitura de arquivo
        try: # Tenta ler o arquivo
            with open(arquivoTexto) as arquivo: # Caso haja um arquivo para ser lido, realiza a leitura
                palavras = [] # Cria uma lista vazia para as palavras no arquivo
                
                for linha in arquivo.readlines(): # Para cada linha do arquivo
                    palavras.extend(linha.split()) # Adiciona cada uma das palavras à lista
                    
                print(automato(palavras, transicao)) # Chama a função automato com a cadeia e o dicionário
                break # Sai do programa após a execução
                
        except: # Se não encontrar o arquivo
            print('Arquivo não encontrado! Verifique o nome digitado e tente novamente') # Continua no loop