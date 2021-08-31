#!/usr/bin/env python
# coding: utf-8

# ## Questionário 22 (Q22)

# **Orientações para submissão:** 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-a à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# 
# <hr>

# **Questão 1**. O texto abaixo é uma mensagem encriptada. Cada grupo de 4 caracteres corresponde a um número hexadecimal.

# ```
# 0x45 0x6d 0x20 0x61 0x6c 0x67 0x75 0x6d 0x20 0x6c 0x75 0x67 0x61 0x72 0x2c 0x20 0x61 0x6c 0x67 0x6f 0x20 0x69 0x6e 0x63 0x72 0xed 0x76 0x65 0x6c 0x20 0x65 0x73 0x74 0xe1 0x20 0x65 0x73 0x70 0x65 0x72 0x61 0x6e 0x64 0x6f 0x20 0x70 0x61 0x72 0x61 0x20 0x73 0x65 0x72 0x20 0x64 0x65 0x73 0x63 0x6f 0x62 0x65 0x72 0x74 0x6f 0x2e
# ```

# Use seus conhecimentos de funções _built_in_ para decodificar a mensagem, que é inteligível na Língua Portuguesa. Em seguida, determine quais são os caracteres da mensagem que correspondem, respectivamente, ao maior e menor valor binário entre os elementos da sequência. Assinale a alternativa que melhor descreve a mensagem decodificada, o caracter associado ao maior valor binário e o caracter associado ao menor valor binário, nesta sequência.
# 
# A. `'Em nenhum lugar, todo possível está aguardando para ser manifesto'`, `'ê'` e `' '`.
# 
# B. `'Em algum lugar, tudo incrível está esperando para ser incompleto.'`, `'s` e  `'a'`.
# 
# C. `'Em nenhum lugar, algo possível deve aguardar para ser descoberto'`, `'ê'` e `'í'`.
# 
# D. `'Em algum lugar, algo incrível está esperando para ser descoberto.'`, `'í` e  `' '`.
# 
# _Obs.:_ Considere que os espaços na mensagem original não devem ser considerados como caracteres na mensagem decodificada e que ali servem apenas para separar os quartetos hexadecimais.

# **Questão 2**. Rindalve é um jovem promissor que conquistou um excelente emprego, mas sofre com a indisciplina financeira. Ele paga o aluguel da casa onde mora sempre com atraso de alguns dias e, extrapola o limite do cartão de crédito com frequência. Neste mês, Jonas pagou seu aluguel de <span> R&#36;</span> 6.500,00 com 12 dias de atraso e hoje faz 6 dias que a fatura de seu cartão, fechada em <span> R&#36;</span> 7.234,77, venceu. 
# 
# A imobiliária que administra a casa de Jonas usa a seguinte regra para calcular o valor adicional devido em caso de atraso no pagamento do aluguel:
# 
# - mora de 6,25% sobre o valor do aluguel + juro simples de 0,025% ao dia
# 
# A administradora de seu cartão de crédito, por outro lado, usa a seguinte regra para calcular o valor adicional devido em caso de atraso no pagamento da fatura do cartão:
# 
# - juro composto de 1,44% ao dia.
# 
# Crie uma função para calcular o valor total atualizado $V_T$ que Jonas deverá desembolsar, em reais, para quitar as despesas citadas. Então, marque a alternativa correta.
# 
# A. <span> R&#36;</span> 19.048,09
# 
# B. <span> R&#36;</span> 19.396,08
# 
# C. <span> R&#36;</span> 14.166,77
# 
# D. <span> R&#36;</span> 16.396,77

# **Questão 3**. O Ministério da Saúde disponibiliza uma lista de remédios através do programa _Farmácia Popular_. Clicando [aqui](https://antigo.saude.gov.br/images/pdf/2019/janeiro/07/Lista-Medicamentos.pdf), você será redirecionado a uma dessas listas. Crie um _dict_ em Python com as informações relevantes contidas na tabela do arquivo PDF. Em seguida, crie uma função regular que recebe o seu _dict_ como argumento e retorne 3 objetos: um _str_, um _tuple_ e um _int_, os quais nesta, ordem, responderão às seguintes perguntas: 
# 
# - Para que doença a maior quantidade de remédios na gratuidade é indicada? 
# - Qual é a quantidade de remédios nas classes _gratuidade_ e _copagamento_?
# - Quantos remédios têm a letra C como inicial de seu nome?
# 
# Assinale a alternativa correta.
# 
# Assinale a alternativa correta:
# 
# A. `'HIPERTENSÃO', (20, 15), 3`  
# 
# B. `'ASMA', (20, 15), 7`
# 
# C. `'DIABETES', (10, 20), 8`
# 
# D. `'ASMA', (18, 17), 6`
# 
# 
# _Obs.:_ tente usar funções anônimas sempre que possível.
