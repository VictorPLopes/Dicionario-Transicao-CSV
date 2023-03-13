# **Dicionario-Transicao-CSV**
## Gera um dicionário de transição à partir de um arquivo CSV e executa a validação de cadeias de caracteres através de um autômato.

Criado para uso na disciplina de Linguagens Formais e Autômatos, do 5º semestre do curso de Engenharia de Computação do Instituto Federal de Educação, Ciência e Tecnologia de São Paulo, Campus Piracicaba. Baseado no algoritmo original do Prof. Dr. Osvaldo Severino Junior.

## Como usar
1. Antes de executar o script, crie um arquivo CSV contendo uma tabela de transição de estados. A primeira linha da tabela é uma lista dos terminais da gramática, a primeira coluna são todos os possíveis estados que o autômato pode assumir e as transições de estados são os nomes dos próximos estados que o autômato assume ao ler o terminal de sua coluna enquanto no estado de sua linha:
![tabela|25%](https://user-images.githubusercontent.com/77900343/224821342-486ec1e7-ccba-4dcb-9e08-11ea977f7381.png)

2. Execute o script e insira o nome (ou caminho) do arquivo CSV gerado a partir da tabela.

3. Caso deseje validar um texto contido em um arquivo, digite seu nome ou caminho. Caso contrário pressione ENTER e insira a(s) palavra(s) manualmente.
