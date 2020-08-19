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

file_to_be_analyzed = "file_to_be_analyzed.txt"

palavras_reservadas = ['while','do']
operadores = ['<','=','+']
terminador_linha = [';',]
identificadores = ['i','j']
numeros = ['0','1','2','3','4','5','6','7','8','9']

# arquivos de saídas
tabela_tokens = open('tabela_tokens.csv', 'w', encoding="utf-8")
tabela_simbolos = open('tabela_simbolos.csv', 'w', encoding="utf-8")

with open(file_to_be_analyzed, "r") as file_handler:
    rows = file_handler.readlines()
    m = 0

    token1 = palavras_reservadas
    token2 = operadores
    token3 = terminador_linha
    token4 = identificadores
    token5 = numeros

    for row in rows:
        lista = []
        termo = ''
        for col in range(len(row)):

            if (row[col] in token3):
                lista.append(row[col])              
            elif (row[col] in token2):
                lista.append(row[col])
            elif row[col] != ' ':
                termo = termo + row[col]
            else:
                lista.append(termo)
                termo = ''

        col=0
        espacos = 0
        tam = 0
        i = 1

        for token in lista:

            if token in token1:
                tabela_tokens.write('{},palavra reservada,{},{},{}\n'.format(token,len(token),m,espacos + tam))

            elif token in token2:
                tabela_tokens.write('{},operador,{},{},{}\n'.format(token,len(token),m,espacos + tam))
              
            elif token in token3:
                tabela_tokens.write('{},terminador de linha,{},{},{}\n'.format(token,len(token),m,espacos + tam))

            elif token in token4:
                tabela_tokens.write('{},identificador,{},{},{}\n'.format(token,len(token),m,espacos + tam))
            
            else:
                eh_numero = False
                for caract in token:
                    if caract in token5:
                        eh_numero = True
                if eh_numero:
                    tabela_tokens.write('{},número,{},{},{}\n'.format(token,len(token),m,espacos + tam))                

            if token != '':
                tabela_simbolos.write('{},{}\n'.format(i,token))
            
            i += 1
            espacos += 1
            tam += len(token)
        m += 1