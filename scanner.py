# RESTRIÇÕES
# não utilizar regex
# não utilizar split

# arquivo a ser analisado : file_to_be_analyzed
# nome do manipulador do arquivo: file_handler
# método readline() para ler uma linha do arquivo, gera uma lista com o conteúdo de cada linha por posição na lista

# inserir token na tabela de tokens
# token(tk) identificação(id) tamanho(ta) posição(po) (linha,coluna)
# while palavra reservada 5 (0,0)
# Parar o scanner ao encontrar o erro: Token desconhecido na posição (x,y)

file_to_be_analyzed = "informar_nome_do_arquivo.txt"

palavras_reservadas = {
    'w':'while',
    'd': 'do',
}
operadores = [ ' < ',' = ',' + ']
terminador_linha = [';',]
identificadores = ['i','j']
numeros = ['0','1','2','3','4','5','6','7','8','9']

# arquivos de saídas
tabela_tokens = open('tabela_tokens.csv', 'w', encoding="utf-8")
tabela_simbolos = open('tabela_simbolos.csv', 'w', encoding="utf-8")

with open(file_to_be_analyzed, "r") as file_handler:
    rows = file_handler.readlines()
    m = 0
    for row in rows:
        m += m
        token1 = palavras_reservadas
        token2 = operadores
        token3 = terminador_linha
        token4 = identificadores
        token5 = numeros
        lista = []
        for col in range(len(row)):
            if token1.get(row[col]):
                tabela_tokens.write('{},palavra reservada,{},({},{})\n'.format(token1.get(row[col]),len(token1.get(row[col])),m,col))
                #col += len(token1.get(row[col]))
            
            elif row[col] in token2:
                tabela_tokens.write('{},operador,{},({},{})\n'.format(row[col],len(row[col]),m,col))
                
            elif row[col] in token3:
                tabela_tokens.write('{},terminador de linha,{},({},{})\n'.format(row[col],len(row[col]),m,col))

            elif row[col] in token4:
                tabela_tokens.write('{},identificador,{},({},{})\n'.format(row[col],len(row[col]),m,col))
            
            elif row[col] in token5:
                if row[col] != ' ':
                    lista.append(row[col])
                    print(lista)
                    numero = ''
                    for n in lista:
                        numero = '{}{}'.format(numero,n)
                tabela_tokens.write('{},número,{},({},{})\n'.format(numero,len(lista),m,col))