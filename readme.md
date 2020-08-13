Resultado da implementação de um analisador léxico para analisar um programa-fonte considerando as seguintes características da linguagem:

* palavras reservadas: while, do
* operadores: <, =, +
* terminador de linha: ;
* identificadores: i, j
* constantes: sequência 1 ou mais números
* números: 0, 1, 2, ..., 9

Ao concluir a análise o programa deve gerar duas saídas (conforme slide 20 do material da aula do dia 5/8):

* tabela de tokens
* tabela de símbolos

# RESTRIÇÕES
# não utilizar regex
# não utilizar split

O formato da saída fica a seu critério (ex.: CSV, JSON)

Se ocorrer um erro de análise léxica durante a análise do programa-fonte o analisador deve interromper o processo e informar a coluna em que o erro aconteceu (opcionalmente, informe o motivo do erro).